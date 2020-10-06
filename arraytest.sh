#!/bin/bash
cd `dirname $0`

a=()
b=("test1", "test2", test3, "this is test")
count=0

func1() {
    a=($RANDOM "${a[@]}")
    count=$((++count))
}
func2() {
    a=(`cat /dev/urandom | tr -dc 'a-zA-Z' | fold -w 5 | head -n 1` "${a[@]}")
    count=$((++count))
}
func3() {
    a=(3 "${a[@]}")
    count=$((++count))
}

echo -e " showを入力で配列を確認 \\n 1を押すとランダムな整数を配列に追加 \\n 2を押すとランダムな5文字の文字列を配列に追加 \\n 3を押すと3を配列に追加 \\n 4を押すとテスト表示 \\n resetを入力で配列リセット \\n qを押すと終了します。 \\n Ctrl+Cでも終了可能です。"

while :
do
read key
case "$key" in
"show")
echo "${a[@]}"
;;
"1")
func1
echo "${a[@]}"
#echo "$count"
;;
"2")
func2
echo "${a[@]}"
#echo "$count"
;;
"3")
func3
echo "${a[@]}"
#echo "$count"
;;
"4")
echo "${b[@]}"
;;

"q")
echo "終了します。"
exit 0
;;

"reset")
unset a[@]
echo "配列は消去されました。"
;;
*)
echo "そのコマンドは認識できません。もう一度何か入力してください。"
;;
esac

done

exit 0
