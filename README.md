# 2020-elex-promos

Simple Python and shell script to update the JSON powering the promo boxes on the 2020 Democratic Primary results page.

To use this repository, you'll need to create a .env file containing your AWS credentials as well as the name of the S3 bucket you're pushing to.

This is extremely hacky and slightly tedious, but it works.

## Instructions

1. Clone the repository
1. cd into the repository and run `pipenv install`
1. Go to the Google Sheet and copy the contents into `wire.csv` and `local.csv`
1. `./json_to_s3.sh` will convert csvs to json. (Note, you will need to give this script file owner execution permissions. `chmod 755 json_to_s3.sh` should do the trick).
1. Copy/paste the contents of `local.json` and `wire.json` to the corresponding fields in  `elex_controls.json`.
1. **BEFORE RUNNING THIS COMMAND READ THE DOCUMENTATION BELOW:** If you are in an activated environment, simply run `python s3.py` to run the script. If your environment is not active `pipenv run python s3.py` should work.

## elex_controls.demographic

The third portion of `elex_controls.json` is the json file that houses the manual controls for the demographic charts. Here's what it controls.

- show_maps - this is a true/false value that controls whether the density maps are shown.
- show_bubbles - this is a true/false value that controls whether the div housing demographic charts is shown.
- show_trump - this specifically controls the trump chart
- trump_text - chatter for the trump chart
- show_nonwhite - this specifically controls the nonwhite chart
- nonwhite_text - chatter for the nonwhite chart
- show_income - this specifically controls the income chart
- income_text - chatter for the income chart
- show_age - this specifically controls the age chart
- age_text - chatter for the age chart
