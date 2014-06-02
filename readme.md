###Export Bibliographic Records for Large Koha Catalogs

This is primarily for hosted Koha catalogs as I am sure there is a much easier way to dump your catalog data if you are hosting it yourself or have access to the server that is hosting it. 

If your Koha instance is hosted, you can export your data from the admin interface, but I have found that it will timeout should you want to export more than 5,000 - 10,000 bibibliographic records. 

If like many libraries you have records on the order of hundreds of thousands to millions, it can be quite tedious to export in these small chunks manually. This script is pretty basic but will do all the work of downloading your catalog while you can focus on something else (anything else).

####Usage

You will only need to install the `mechanize` module for this to work.

`easy_install mechanize` documentation [here](http://wwwsearch.sourceforge.net/mechanize/download.html)

copy the `koha_config-example.py` file as `koha_config.py` and modify the configurations to match your setup.

This script could be done way more flexibly, with more configurability, but I don't think something like this is in high demand so it is distributed as is.

####Notes

Again, this script is for automating the process of downloading all records and is not configured to handling customized chunks in between (though if you were to set the `start` variable to something other than `1`, it would start at that bib record, of course)

The way this handles total records in increments is pretty lazy. So if you have 246000 bibliographic records, and you set the increment to 5000, it is going to miss those last 1000. You can avoid this by rounding up the total number of records by a magnitude of the increment you've set. So if you have 246000 records, just set the `total` to 250000.  



