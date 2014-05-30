###Export Bibliographic Records for Large Koha Catalogs

This is primarily for hosted Koha catalogs as I am sure there is a much easier way to dump your catalog data if you are hosting it yourself or have access to the server that is hosting it. 

If your Koha instance is hosted, you can export your data from the admin interface, but I have found that it will timeout should you want to export more than 5,000 - 10,000 bibibliographic records. 

If like many libraries you have records on the order of hundreds of thousands to millions, it can be quite tedious to export in these small chunks manually. This script is pretty basic but will do all the work of downloading your catalog while you can focus on something else (anything else).
