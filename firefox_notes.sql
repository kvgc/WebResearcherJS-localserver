.headers on
.mode csv
.once /Destination_Folder/saved_notes.csv
select * from webappsstore2 WHERE  value like "%pell-content%";
