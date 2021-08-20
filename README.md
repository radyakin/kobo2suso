# kobo2suso
Converter of questionnaires from Kobo Toolbox to Survey Solutions.

Sergiy Radyakin, Thе Wоrld Bаnk, 2021.

![](kobo2suso.jpg)

### Python Syntax

```
from kobo2suso import koboConvert
koboConvert("kobo.xlsx","suso.zip")
```

### Compatibility Notes
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
- Formatting - not transferred (not clear if supported in original files.)

##### **Question types**:
- Text (*"text"*)
- Numeric (*"integer"*, *"decimal"*)
- Single-select (*"select_one"*)
- Multiple-select (*"select_multiple"*)
- Date (*"date"*)
- Image (*"image"* and *"image signature"*) (untested)

### No-equivalent

It appears at the moment that the following attributes in the source format do not have an equivalent attribute in the destination format:

- read-only;
- required;
- default.

### Useful Links to Products and Standards

* Kobo Toolbox homepage: https://www.kobotoolbox.org/
* Survey Solutions homepage: https://mysurvey.solutions

* Description of XLSForms standard: https://xlsform.org/
* ESRI description of XLSForms as implemented in ArcGIS Survey123: https://doc.arcgis.com/en/survey123/desktop/create-surveys/xlsformessentials.htm
* ODK import to Stata by Matthew White: http://fmwww.bc.edu/RePEc/bocode/o/odkmeta.sthlp
