echo "ctrl+c out of this script if tor isnt on and put your query(s) in a txt starting in 5 seconds"
sleep 5
echo "how many pages do you wanna scrape? (the more the longer it takes)"
read pagenum
echo "keyword file"
read keywordfile
torsocks GoogleScraper -s duckduckgo --keyword-file $keywordfile -p $pagenum --output-filename rawout.json
dos2unix rawout.json
mv rawout.json rawout.txt
cat rawout.txt | grep "https://throwbin.io/" > linkout.txt
sed 's/^.\{15\}//g' linkout.txt > filteredlinkout.txt
sed 's/..$//' < filteredlinkout.txt > doublefiltered.txt
rm filteredlinkout.txt
rm linkout.txt
sed '/^.\{27\}./d' doublefiltered.txt > triplefiltered.txt
sed -i 's/\(.\{20\}\)//' triplefiltered.txt
mv triplefiltered.txt pasteids.txt
awk '{print "https://api.throwbin.io/v1/paste/"$0}' pasteids.txt > leechedlinks.txt
rm pasteids.txt
rm doublefiltered.txt
rm rawout.txt
rm google*
