cd ..
cd data/output
for d in */; do
    echo $d
    zip -r ${d%/}.zip $d
done

