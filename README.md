# Elasticsearch Index Clear Script

This script connects to an Elasticsearch instance and deletes all indices.

## Requirements

- Python 3.7 or higher
- Elasticsearch instance running locally on `http://localhost:9200`

## Dependencies

The script requires the following Python packages:

- `certifi==2024.7.4`
- `elastic-transport==8.13.1`
- `elasticsearch==8.14.0`
- `urllib3==2.2.2`
- and others listed in the `requirements.txt`

## Setup

### Step 1: Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/hr-sobuj/es-script.git
cd es-script
```

### Step 2: Create and Activate a Virtual Environment

It is recommended to create a virtual environment to manage your dependencies. You can do this using the following commands:

```bash
# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
# On Windows:
.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate
```

### Step 3: Install Dependencies

Once the virtual environment is activated, install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Script

To run the script and delete all indices from your Elasticsearch instance, use the following command:

```bash
python main.py
```

Make sure to replace `'url'` `'username'` and `'password'` in the script with your actual Elasticsearch credentials.

## Notes

- **Warning:** This script will delete **all indices** in the connected Elasticsearch instance. Use with caution.
- Ensure that the Elasticsearch service is running locally and accessible at `http://localhost:9200`.

