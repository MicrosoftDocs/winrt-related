---
ms.assetid: 13623913-5515-41e8-929e-e57d8aa38635
title: rescap3:MigrationProgIds (child of uap:FileTypeAssociation)
description: Contains Migration Prog Ids for protocols and file type associations.
ms.date: 04/05/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# rescap3:MigrationProgIds (child of uap:FileTypeAssociation)

Contains [programmatic identifier (ProgID)](/windows/win32/shell/fa-progids) values that describes the application, component, and version of each desktop application from which you want to inherit file associations.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:Extension\>](element-uap-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:FileTypeAssociation\>](element-uap-filetypeassociation.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<rescap3:MigrationProgIds\>**

## Syntax

```xml
<rescap3:MigrationProgIds>

  <!-- Child elements -->
  rescap3:MigrationProgId{0,10000}

</rescap3:MigrationProgIds>
```

### Key

`{}` specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [rescap3:MigrationProgId](element-rescap3-migrationprogid.md) | Contains a migration Prog Id string for protocols and file type associations. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap:FileTypeAssociations](element-uap-filetypeassociation.md) | Declares an app extensibility point of type **windows.fileTypeAssociation**. A file type association indicates that the app is registered to handle files of the specified types. |

## Requirements

| Item | Value                                                       |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities/3` |
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |
