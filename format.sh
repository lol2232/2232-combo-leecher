#echo input file?
#read input
cat output.txt | cut -d ' ' -f 1 > output2.txt
cat output2.txt | cut -d '|' -f 1 > usermailmix.txt
cat usermailmix.txt | grep -v @ > usercombo.txt
cat usermailmix.txt | grep @ > emailcombo.txt
rm usermailmix.txt
sed "/\:$/d" usercombo.txt > userpass.txt
mv userpass.txt usercombo.txt
cat usercombo.txt | grep : > userpass.txt
mv userpass.txt usercombo.txt
sed "/\\w$/d" usercombo.txt > userpass.txt
mv userpass.txt usercombo.txt
rm output2.txt
find -size 0 -delete
