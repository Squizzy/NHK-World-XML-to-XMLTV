# NHK World EPG to XMLTV converter

- Extracts NHK World's EPG in JSON from its website
- Converts it to an XMLTV file
- Outputs the XMLTV file to the current directory

- A python 3.x and a separate python 2.7 versions are available

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

### Python2

the __p2__ branch of this repository contains the python v2 version, as per external contributor dazzhk recommendation.  
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

## Note:
All other files in this repository have no value and are only here for historical reason (until they are removed)

## Version history

20250715 - v1.4
    - Merged refactored Python3 version of CreateNHKXMLTV.py into master branch.
    - Corrected requirement.txt -> requirements.txt .

20240502 - v1.3
    - Version change to represent the refactored Python3 version of CreateNHKXMLTV.py in its devel branch.

20240415 - v1.2
    - updated the URL for the NHK world EPG JSON as per external contributor fxbx recommendation
    - replaced deprecated utcfromtimestamp(), added timeOffsetVariable
    - cleaned up XML tree generation
    - added some new genres

20190120 - v1.1
    - changed to pulling the file from URL
    - windows executable created using "auto-py-to-exe.exe .\CreateNHKXMLTV.py" (auto-pi-to-exe v2.5.1)\
      File to be found under "output" folder. Not virus checked.

20190119 - v1.0.5
    - add second category (genre) for channels which have it

20190119 - v1.0.4
    - corrected \<category\> (genre) to use all lowercase

20190119 - v1.0.3
    - corrected \<Icon\> typo source xml

20190119 - v1.0.2
    - added header, version, licence, and reference URL for later

19 Jan 2019 - v1.0.1
    - Some tidying up

20190119 - v1.0
    - First release as working version
