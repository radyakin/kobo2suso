# kobo2suso
Converter of questionnaires from Kobo Toolbox to Survey Solutions.

Sergiy Radyakin, Thе Wоrld Bаnk, 2021.

### Links to products

* Kobo Toolbox homepage: https://www.kobotoolbox.org/
* Survey Solutions homepage: https://mysurvey.solutions


### Python Syntax

```
from kobo2suso import koboConvert
koboConvert("kobo.xlsx","suso.json")
```

### Compatibility Notes
- Excel file must have a sheet with the specific name "survey";
- Excel file must have specific positions of columns:
  - type in column C;
  - name in column D;
  - English label in column E;
  - English hint in column F;

- Sections/sub-sections transferred. Repetitions not supported.
- Notes are transferred as static texts;
- Question texts - transferred for some* question types;
- Variable names - transferred for some* question types, not validated against Survey Solutions requirements;
- Hints - transferred as instructions for some* question types;
- Text substitution placeholders are transferred, for example: "*How old is ${name}?*" will appear as "*How old is %name%?*"
- Categories of single select questions - not transferred;
- Enabling conditions - not transferred;
- Validation conditions - not transferred;
- Calculated variables - not transferred (skipped).
- Formatting - not transferred (not clear if supported in original files.)



##### ***Question types**:
- Text
- Numeric
- Single-select
