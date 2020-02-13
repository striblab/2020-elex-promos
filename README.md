# 2020-elex-promos

Simple Python and shell script to update the JSON powering the promo boxes on the 2020 Democratic Primary results page.

To use this repository, you'll need to create a .env file containing your AWS credentials as well as the name of the S3 bucket you're pushing to.

## Instructions

1. Clone the repository
2. cd into the repository and run `pipenv install`
3. `./json_to_s3.sh` will run the script. (Note, you will need to give this script file owner execution permissions. `chmod 755 json_to_s3.sh` should do the trick).
