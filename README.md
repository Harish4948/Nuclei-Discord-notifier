# Nuclei-Discord-notifier
Just a python script which I built when I had to run nuclei on a list of file on my VPS.

## Description

The script runs nuclei under screen(useful when running on VPS) on a list of files in format file*.txt.

The script notifies whenever it starts a file scan.Then noties the findings by splitting into five different categories(info,low,medium,high,critical) 
in five different channels. Since Discord has rate limit and I couldn't just fire off live findings So I have made it notify on file output 
and made sure to chunk the output in parts to not get rate limited.

## USAGE

Create five different channels in discord(info,low,medium,high,critical) and paste the webhook in the function discord_output_split.
Create a general channel for pinging the status of scans and paste the discord token in the main for loop i.e deindented for loop

Customize the iterations in the main for loop according to your needs.(Since I had less ram, I made one run on even number of files and other on Odd).

## Eg File Format
file00.txt,file21.txt...
