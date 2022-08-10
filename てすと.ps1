cd ~/Desktop/
$i = 1

while ($i -le 10){
    if (-not (test-path ~/Desktop/ネットワーク調査結果_$i) ){
        write-Host "ネットワーク調査結果_$i フォルダがありません。　フォルダを作成しますか？"
        ####################　選択肢　####################
        # yes なら 0 / no なら 1
        #選択肢の作成
        $typename = "System.Management.Automation.Host.ChoiceDescription"
        $yes = new-object $typename("&Yes","実行する")
        $no  = new-object $typename("&No","実行しない")
        #選択肢コレクションの作成
        $choice = [System.Management.Automation.Host.ChoiceDescription[]]($yes,$no)
        #選択プロンプトの表示
        $answer = $host.ui.PromptForChoice("<実行確認>","実行しますか？",$choice,0)
        ##################################################
        Write-Output -InputObject $answer

        if($answer -eq 0){
           New-Item "ネットワーク調査結果_$i" -ItemType Directory
            Write-Output -InputObject "フォルダを作成します。"
            

                ####################　処理　####################
                
                ##################　環境情報　###################
                # システム情報取得
                $ReturnData = New-Object PSObject | Select-Object HostName,Manufacturer,Model,SN,CPUName,PhysicalCores,Sockets,MemorySize,OS
                $Win32_BIOS = Get-WmiObject Win32_BIOS
                $Win32_Processor = Get-WmiObject Win32_Processor
                $Win32_ComputerSystem = Get-WmiObject Win32_ComputerSystem
                $Win32_OperatingSystem = Get-WmiObject Win32_OperatingSystem
                # ホスト名
                $ReturnData.HostName = hostname

                # メーカー名
                $ReturnData.Manufacturer = $Win32_BIOS.Manufacturer
                # モデル名
                $ReturnData.Model = $Win32_ComputerSystem.Model
                # シリアル番号
                $ReturnData.SN = $Win32_BIOS.SerialNumber
                # CPU 名
                $ReturnData.CPUName = @($Win32_Processor.Name)[0]
                # 物理コア数
                $PhysicalCores = 0
                $Win32_Processor.NumberOfCores | % { $PhysicalCores += $_}
                $ReturnData.PhysicalCores = $PhysicalCores    
                # ソケット数
                $ReturnData.Sockets = $Win32_ComputerSystem.NumberOfProcessors
                # メモリーサイズ(GB)
                $Total = 0
                Get-WmiObject -Class Win32_PhysicalMemory | % {$Total += $_.Capacity}
                $ReturnData.MemorySize = [int]($Total/1GB)
                # OS 
                $OS = $Win32_OperatingSystem.Caption
                $SP = $Win32_OperatingSystem.ServicePackMajorVersion
                if( $SP -ne 0 ){ $OS += "SP" + $SP }
                $ReturnData.OS = $OS

                #Write-Output $ReturnData | Add-Content ./ネットワーク調査結果_$i/result.txt -Encoding UTF8  
                Write-Output $ReturnData | Export-Csv -Path ./ネットワーク調査結果_$i/machineinfo.csv -Encoding UTF8 -NoTypeInformation
                ##################################################
                
                Get-NetAdapter | Export-Csv -Path  ./ネットワーク調査結果_$i/netadapter.csv -Encoding UTF8 -NoTypeInformation

                ##################################################
        $i=100
        }
        else{
            Write-Output -InputObject "キャンセルします。"
#            # 何もしない
#           Write-Output -InputObject "何かキーを押して下さい"
#            $host.UI.RawUI.ReadKey()
        exit
        }
    }
    else{
        write-Host "ネットワーク調査結果_$i が存在します。スキップします。"
        $i++
        Write-Output -InputObject "続行するには何かキーを押して下さい . . . "
        $host.UI.RawUI.ReadKey()
    }
}

function getnetconfig{
    $result1 = Get-NetIPConfiguration
    
}

