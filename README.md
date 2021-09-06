# kobo2suso
Converter of questionnaires from Kobo Toolbox to Survey Solutions.

Sergiy Radyakin, Thе Wоrld Bаnk, 2021.

![](kobo2suso.jpg)

The program takes as input XLSForms files (like
[this example](https://github.com/SEL-Columbia/formhub/blob/master/static/tutorial/tutorial.xls?raw=true))
and produces files in the format that Survey Solutions understands.


### Python Syntax

```
from kobo2suso import koboConvert
koboConvert("kobo.xlsx","suso.zip")
```

### Requires

The program has been developed and tested with Python version 3.8.1 and
requires the following additional modules to be installed:

- [openpyxl](https://pypi.org/project/openpyxl/)
- [markdown](https://pypi.org/project/Markdown/)


### Compatibility Notes
- Works with *.xlsx files, not *.xls files (resave using Excel if you get an *.xls file);
- Excel file must have a sheet with the specific name "survey", and (if categories are present) a specific sheet "choices";
- Specific positions of columns storing *type*, *name*, *label* and *hint* for questions will be determined automatically in the Excel file. *Hint* is optional, while other columns are required.
- Sections/sub-sections are transferred. Repetitions not supported.
- Notes are transferred as static texts;
- Question texts - transferred for some* question types;
- Variable names - transferred for some* question types, not validated against Survey Solutions requirements;
- Hints - transferred as instructions for some* question types;
- Text substitution placeholders are transferred, for example: "*How old is ${name}?*" will appear as "*How old is %name%?*"
- Categories of single-select and multiple-select questions - tentatively supported (if numeric, for non-numeric categories new numeric codes will be assigned); If there are more than 200 categories, may need to switch to combobox presentation in Survey Solutions (compiler will tell that).
- Relevance (enabling) conditions - not transferred;
- Restriction (validation) conditions - not transferred;
- Calculated variables - not transferred (skipped).
- Formatting - tentatively transferred (not clear what is supported in original files, currently markdown is converted to corresponding HTML. If original formatting included hyperlinks, those will be lost, as links must remain in markdown for Survey Solutions.)
- The following elements are converted into explanatory notes:
  - start;
  - end;
  - today;
  - username;
  - deviceid;
  - subscriberid;
  - phonenumber;
  - simserial;
  - audit.

##### **Question types**:

- Text (*"text"*)
- Numeric (*"integer"*, *"decimal"*)
- Single-select (*"select_one"*)
- Multiple-select (*"select_multiple"*)
- Date (*"date"*)
- Image (*"image"* and *"image signature"*) (untested)
- GPS location (*"geopoint"*)
- Audio (*"audio"*)


### Audit

[Audit option in XlsForms](https://docs.getodk.org/form-audit-log/) indicates
that the paradata needs to be recorded. This is always true for Survey
Solutions and can't be turned on or off. Note, however, that the paradata
recording in Survey Solutions does not contain location coordinates for
every event.


### No-equivalent

It appears at the moment that the following attributes in the source format do
not have an equivalent attribute in the destination format:

- read-only;
- required;
- default.

Survey Solutions does not allow control over the quality of the audio recording
(voice-only, low and normal) in audio recording questions.

Survey Solutions does not directly allow the calculated variables to have
conditional enablement (relevance in XlsForms terminology). All calculated
variables are calculated if they are part of the enabled scope (a section or a
subsection).

Survey Solutions does not allow calculated variables to be of undefined types,
whereas XlsForms-based systems seem to permit this (the same variable may be
of string or numeric type, depending on the calculation path). One approach of
handling this may be to use relevance condition as part of the calculation
expression, such as:
```
(relevance_expression) ? (calculation_expression) : null
```


### Aliases
According to
[this source](https://github.com/XLSForm/pyxform/blob/master/pyxform/aliases.py)
there are numerous aliases to the question types (for example: *"select1"*,
*"select_one"*, *"select one"*, *"select one from"*, etc). This tool does not
recognize them all and uses question types as mentioned above (in this example
*"select_one"*).

### Compatible Products

According to [xlsforms.org](https://xlsform.org/en/#tools-that-support-xlsforms)
the tools that support XLSForms:

* CommCare
* ODK
* Enketo
* Tattara
* DataWinners
* Ona
* Community Health Toolkit
* SurveyCTO
* Secure Data Kit (SDK)
* KoBoToolBox
* Survey123 for ArcGIS


### Useful Links to Products and Standards

* Kobo Toolbox homepage: https://www.kobotoolbox.org/
* Survey Solutions homepage: https://mysurvey.solutions

* Description of XLSForms standard: https://xlsform.org/
* XLSForms reference table: https://xlsform.org/en/ref-table/
* KoBoToolbox documentation page: https://kobotoolbox-documentation.readthedocs.io/en/latest/welcome.html
* ESRI description of XLSForms as implemented in ArcGIS Survey123: https://doc.arcgis.com/en/survey123/desktop/create-surveys/xlsformessentials.htm
* ODK documentation page: https://docs.getodk.org/
* ODK import to Stata by Matthew White: http://fmwww.bc.edu/RePEc/bocode/o/odkmeta.sthlp
* Ona documentation page: https://help.ona.io/knowledge-base/guide-creating-surveys/
* Enketo homepage: https://enketo.org/
