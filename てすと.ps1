cd ~/Desktop/
$i = 1

while ($i -le 10){
    if (-not (test-path ~/Desktop/�l�b�g���[�N��������_$i) ){
        write-Host "�l�b�g���[�N��������_$i �t�H���_������܂���B�@�t�H���_���쐬���܂����H"
        ####################�@�I�����@####################
        # yes �Ȃ� 0 / no �Ȃ� 1
        #�I�����̍쐬
        $typename = "System.Management.Automation.Host.ChoiceDescription"
        $yes = new-object $typename("&Yes","���s����")
        $no  = new-object $typename("&No","���s���Ȃ�")
        #�I�����R���N�V�����̍쐬
        $choice = [System.Management.Automation.Host.ChoiceDescription[]]($yes,$no)
        #�I���v�����v�g�̕\��
        $answer = $host.ui.PromptForChoice("<���s�m�F>","���s���܂����H",$choice,0)
        ##################################################
        Write-Output -InputObject $answer

        if($answer -eq 0){
           New-Item "�l�b�g���[�N��������_$i" -ItemType Directory
            Write-Output -InputObject "�t�H���_���쐬���܂��B"
            

                ####################�@�����@####################
                
                ##################�@�����@###################
                # �V�X�e�����擾
                $ReturnData = New-Object PSObject | Select-Object HostName,Manufacturer,Model,SN,CPUName,PhysicalCores,Sockets,MemorySize,OS
                $Win32_BIOS = Get-WmiObject Win32_BIOS
                $Win32_Processor = Get-WmiObject Win32_Processor
                $Win32_ComputerSystem = Get-WmiObject Win32_ComputerSystem
                $Win32_OperatingSystem = Get-WmiObject Win32_OperatingSystem
                # �z�X�g��
                $ReturnData.HostName = hostname

                # ���[�J�[��
                $ReturnData.Manufacturer = $Win32_BIOS.Manufacturer
                # ���f����
                $ReturnData.Model = $Win32_ComputerSystem.Model
                # �V���A���ԍ�
                $ReturnData.SN = $Win32_BIOS.SerialNumber
                # CPU ��
                $ReturnData.CPUName = @($Win32_Processor.Name)[0]
                # �����R�A��
                $PhysicalCores = 0
                $Win32_Processor.NumberOfCores | % { $PhysicalCores += $_}
                $ReturnData.PhysicalCores = $PhysicalCores    
                # �\�P�b�g��
                $ReturnData.Sockets = $Win32_ComputerSystem.NumberOfProcessors
                # �������[�T�C�Y(GB)
                $Total = 0
                Get-WmiObject -Class Win32_PhysicalMemory | % {$Total += $_.Capacity}
                $ReturnData.MemorySize = [int]($Total/1GB)
                # OS 
                $OS = $Win32_OperatingSystem.Caption
                $SP = $Win32_OperatingSystem.ServicePackMajorVersion
                if( $SP -ne 0 ){ $OS += "SP" + $SP }
                $ReturnData.OS = $OS

                #Write-Output $ReturnData | Add-Content ./�l�b�g���[�N��������_$i/result.txt -Encoding UTF8  
                Write-Output $ReturnData | Export-Csv -Path ./�l�b�g���[�N��������_$i/machineinfo.csv -Encoding UTF8 -NoTypeInformation
                ##################################################
                
                Get-NetAdapter | Export-Csv -Path  ./�l�b�g���[�N��������_$i/netadapter.csv -Encoding UTF8 -NoTypeInformation

                ##################################################
        $i=100
        }
        else{
            Write-Output -InputObject "�L�����Z�����܂��B"
#            # �������Ȃ�
#           Write-Output -InputObject "�����L�[�������ĉ�����"
#            $host.UI.RawUI.ReadKey()
        exit
        }
    }
    else{
        write-Host "�l�b�g���[�N��������_$i �����݂��܂��B�X�L�b�v���܂��B"
        $i++
        Write-Output -InputObject "���s����ɂ͉����L�[�������ĉ����� . . . "
        $host.UI.RawUI.ReadKey()
    }
}

function getnetconfig{
    $result1 = Get-NetIPConfiguration
    
}

