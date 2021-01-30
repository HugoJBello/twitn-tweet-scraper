cd ..
cd data/accounts/scraper_news
for d in */; do
    echo $d
    zip -r ${d%/}.zip $d
    mv ${d%/}.zip ../../zipped_data
done

