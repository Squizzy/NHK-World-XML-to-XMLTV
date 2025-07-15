# NHK World EPG to XMLTV converter

- Extracts NHK World's EPG in JSON from its website
- Converts it to an XMLTV file
- Outputs the XMLTV file to the current directory

## How to run the script

### Python3

Currently hosted only in the __master__ branch of this github repository.  
Two files are needed: CreateNHKXMLTV.py and requirements.txt.

1. In a terminal, create a dedicated folder

    Open a console:

    > Windows, run Command Prompt (cmd.exe) or Powershell (powershell.exe)  
    > MacOS: run Terminal (Terminal.app)  
    > Linux: run Terminal (Terminal)

    Navigate to your preferred location then create the folder, eg:

    ```shell
    mkdir NHK-World-EPG-XMLTV-Extractor
    ```  

    ```shell
    cd NHK-World-EPG-XMLTV-Extractor
    ```

2. Download the required files from the repository

    - Either direct from here (place the files in the folder created earlier):
    > [CreateNHKXMLTV.py](https://github.com/Squizzy/NHK-World-XML-to-XMLTV/blob/master/Python/CreateNHKXMLTV.py)  
    > [requirements.txt](https://github.com/Squizzy/NHK-World-XML-to-XMLTV/blob/master/Python/requirements.txt)

    - or from the terminal:  

    ```shell
    curl -O https://github.com/Squizzy/NHK-World-XML-to-XMLTV/blob/master/Python/CreateNHKXMLTV.py
    ```

    ```shell
    curl -O https://github.com/Squizzy/NHK-World-XML-to-XMLTV/blob/master/Python/requirements.txt
    ```

3. Set up the environment:

    1. From the terminal in the folder created earlier, create a virtual environment in the folder (so all needed modules are isolated locally):

        ```shell
        python3 -m venv venv
        ```

    2. Load the environment:

        - For Windows:

        ```shell
        .\venv\Scripts\activate
        ```

        - For MacOS, Linux:

        ```shell
        source venv/bin/activate
        ```

    3. Load the required modules (Windows, MacOs, Linux):

        ```shell
        pip install -r requirements.txt
        ```

    This is now ready to run.

4. Execute the script

    ```shell
    python CreateNHKXMLTV.py
    ```

5. The XMLTV file created is saved in the same folder as `ConvertedNHK.xml`.

### Python v2

the __p2__ branch of this repository contains the python v2 version, as per dazzhk implementation.  
it is not merged into master yet as it is not tested.

The same procedure as above but:  

1. different files are currently needed (Section 2. of Python3 abobe):

    - Either direct from here (place the files in the folder created earlier):

    > [CreateNHKXMLTV.py](https://github.com/Squizzy/NHK-World-XML-to-XMLTV/blob/p2/Python/CreateNHKXMLTV.py)  
    > [requirements.txt](https://github.com/Squizzy/NHK-World-XML-to-XMLTV/blob/p2/Python/requirements.txt)

    - or from the terminal:  

    ```shell
    curl -O https://github.com/Squizzy/NHK-World-XML-to-XMLTV/blob/p2/Python/CreateNHKXMLTV.py
    ```

    ```shell
    curl -O https://github.com/Squizzy/NHK-World-XML-to-XMLTV/blob/p2/Python/requirements.txt
    ```

2. Python2 executable needs to be used to create the virtual environment (first step of section 3. of Python3 above):

    ```shell
    python3 -m venv venv
    ```

3. Same procedure as above after these two substitutions have been done.

## Background info

NHK World is a Japanese television channel that broadcasts a wide range of programming, including news, sports, and entertainment.
This is information that was collected from different sources.

NHK-World-XML-to-XMLTV
* creating XMLTV file from XML of NHK World

Source info.txt
*  path to the original info, and tools
  
all-json-example.json
*  Save of NHKWorld file with .json used
  
all-xml-example-from-using-url.xml
*  save of NHKWorld file with .XML used
  
convertjson.xml
*  json extracted from the URL converted with the online tool
  
source XML data to transform.xml
*   Unitary source of data to transform
   
NHK World XML to XMLTV converter
*  Path to the XCode CLI file to do the conversion
