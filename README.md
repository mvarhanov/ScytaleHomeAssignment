# Scytale Home Assignment

## Description
### Task:
> #### Extract
> 1. Get the all repository from Organization: Scytale-exercise (https://github.com/Scytale-exercise)
> 2. For each repository in the organization, Get all pull requests.
> 3. Save the data on JSON files.
> #### Transform
> **Please use Pyspark
> 1. Get the JSON files (from the extract phase) .
> 2. Transform the separate files into this table using Spark (Use schema).
> 3. Please save the data to a parquet file.
> 
> 
> | Organization Name            | repository_id            | repository_name            | repository_owner                  | num_prs                               | num_prs_merged                               | merged_at                            | is_compliant                                                                |
> |--------------------------|--------------------------|----------------------------|-----------------------------------|---------------------------------------|----------------------------------------------|--------------------------------------|-----------------------------------------------------------------------------|
> | the first phase before '/' from field `full_name` from repositories | `raw.id` from repositories | `raw.name` from repositories | `raw.owner.login` from repositories | The number of PRs for each repository | The number of Merged PRs for each repository | The last date that a PR was merge in | (`num_prs` == `num_prs_merged`) AND (`repository_owner` contains "scytale") |
> 
> #### Notes
> 1. Not all repositories have a PR.
> 2. PRs merged != PRs closed
> 
> ### Bonus
> - Handle pagination.
> - Handle rate limits.

#### Notes:
1. I didn't add pagination because my implementation doesn't use it.
2. I would suggest changing the name of the Organization Name field to organization_name, since this option is more consistent with the naming style of the remaining fields.

### Installation
#### Prerequisites
* Python 3.11

#### Steps to install project:

```bash
git clone https://github.com/username/repository.git
cd scytale_exercise
pip install -r requirements.txt
```

### Usage
1. Create envs.env file and add in that GITHUB_TOKEN="you_github_token".
2. Run:
```bash
python main.py
```

 This code will run a function that will perform the actions according to the task. JSON files save in project directory json_data. Parquet files save in project directory parquet_data.