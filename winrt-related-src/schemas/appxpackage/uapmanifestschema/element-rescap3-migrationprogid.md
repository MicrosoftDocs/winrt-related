---
title: rescap3:MigrationProgId
description: Contains a migration Prog Id string for protocols and file type associations (descendant of uap:FileTypeAssociation).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, rescap3:Extension, rescap3:FileTypeAssociation, rescap3:MigrationProgIds, rescap3:MigrationProgId, rescap3:Protocol]
---

# rescap3:MigrationProgId

Contains a [programmatic identifier (ProgID)](/windows/win32/shell/fa-progids) value that describes the application, component, and version of a desktop application from which you want to inherit file associations.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<rescap3:Extension>`](element-rescap3-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<rescap3:FileTypeAssociation>`](element-uap-filetypeassociation.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<rescap3:MigrationProgIds>`](element-rescap3-migrationprogids.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<rescap3:MigrationProgId>`**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<rescap3:Protocol>`](element-uap-protocol.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<rescap3:MigrationProgIds>`](element-rescap3-migrationprogids.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<rescap3:MigrationProgId>`**  

## Syntax

```xml
<rescap3:MigrationProgId>
    <!-- TODO: Add value description -->
</rescap3:MigrationProgId>
```

## Value

An alphanumeric string separated by a period with a value between 1 and 39 characters in length (for example, "Foo.Bar" or "Foo.Bar.1").

## Attributes

None.

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [rescap3:MigrationProgIds](element-rescap3-migrationprogids.md) | Contains [programmatic identifier (ProgID)](/windows/win32/shell/fa-progids) values that describes the application, component, and version of each desktop application from which you want to inherit file associations. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities/3` |
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
