## pyEAS
Poll real-time Emergency Alert System (EAS) data via the NWS.
### Setup
First, clone the repository. Install dependencies via:
```
pip install -r requirements.txt
```
### Usage
1. Open `config.json` and put the coordinates of the area you wish to monitor in `point`, i.e.:
```
{
  "point": "41.875562,-87.624421",  
  ...
}
```
2. Run the script via:
```
python eas.py
```
