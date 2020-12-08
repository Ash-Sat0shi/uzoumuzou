#!/bin/bash

echo "過去何日間以前のデータを残すか入力してください ： "
echo "例）　1:今日より前、　2:昨日より前"
#入力された数字をkeyに代入
read key

#---MAIN--------------------------------------------------------------

#もし違うディレクトリいじるなら消すかワーキングディレクトリを別途指定
SOURCE_DIR=`dirname $0`
#指定ディレクトリ内のファイルを配列files内に格納、ファイル形式もここで指定
files=("$SOURCE_DIR"/*)

TODAY=`date +%Y'年'%m'月'%d'日'`
#echo "今日の日付は : $TODAY"
targetdate=`date --date "$key days ago" +%Y'年'%m'月'%d'日'`
echo " $targetdate より前のデータを検索しています……"

#スペース区切りで配列表示　見づらい
#echo "${files[@]}"

#改行区切りで配列表示
for i in "${files[@]}"
    do
        
        #12文字目から8文字切り出し
        #echo ${i:12:8}
        #date -d "${i:12:8}" +%Y%m%d
        hiduke=`echo $i | cut -c 15-22`
        filedate=`date -d "$hiduke" +%s`
        
        if [ `date -d "$filedate" > /dev/null 2>&1; echo $?` -ne 0 ]; then
        
            #date --date "$key days ago" +%Y%m%d で今日よりn日前を出力
            tgtdate=`date --date "$key days ago" +%s`
            #UNIX TIMEで指定した日時からファイル名の日時を引き算
            secdiff=`expr $tgtdate - $filedate`
            #60(sec)x60(min)x24(hour)で86400秒で割って差分の日時を求める
            daydiff=`expr $secdiff / 86400`
            #echo $daydiff
                if [ $daydiff -ge 0 ]; then
                #echo "削除中：$i"
                echo "削除候補 : $i "
                #echo `date -d "$hiduke" +%Y%m%d`
                else
                :
                fi
        else
        echo "日付では無いデータです。削除しません。"
        fi
    done

read -p " 上記データを削除します。よろしいですか？(y/N): " yn
case "$yn" in 
    [yY]*)
    for j in "${files[@]}"
    do

        hiduke=`echo $j | cut -c 15-22`
        filedate=`date -d "$hiduke" +%s`
        if [ `date -d "$filedate" > /dev/null 2>&1; echo $?` -ne 0 ]; then
            tgtdate=`date --date "$key days ago" +%s`
            secdiff=`expr $tgtdate - $filedate`
            daydiff=`expr $secdiff / 86400`
                if [ $daydiff -ge 0 ]; then
                echo "削除中：$j"
                
                #-----削除コマンド-----注意-------------------------
                rm -f "$j"
                
                else
                :
                fi
        else
        :
        fi
    done
    
    ;;
    *) echo "作業をキャンセルしました。" ;
    exit
    ;;
esac



#---削除後の処理-------------------------------------------------------------------
#echo "　削除が完了しました。　ディレクトリ一覧を表示します"
#newfiles=("$SOURCE_DIR"/*)
#for k in "${newfiles[@]}"
#    do echo $k
#done

exit 0