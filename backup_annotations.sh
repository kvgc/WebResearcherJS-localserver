rm webappsstore.sqlite
rm saved_notes.csv
cp /Path/To/webappsstore.sqlite  /Destination_Folder/
sqlite3 webappsstore.sqlite < firefox_notes.sql
