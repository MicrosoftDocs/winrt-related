---
ms.assetid: d144eb77-9888-4fb9-93cb-23308235acc5
title: rescap3:MigrationProgId (descendant of uap:Protocol)
description: Contains a migration Prog Id string for protocols and file type associations (descendant of uap:Protocol).
ms.date: 04/05/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# rescap3:MigrationProgId (descendant of uap:Protocol)

Contains a migration Prog Id string for protocols and file type associations.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:Extension\>](element-uap-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:Protocol\>](element-uap-protocol.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:MigrationProgIds\>](element-rescap3-migrationprogids.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<MigrationProgId\>**

## Syntax

```xml
<rescap3:MigrationProgId> 
    An alphanumeric string with a period separated value between 1 and 39 characters in length (for example, Foo.Bar or Foo.Bar.1).
</rescap3:MigrationProgId>
```

## Attributes and elements

### Attributes

None.

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [rescap3:MigrationProgIds](element-rescap3-migrationprogids.md) | Contains [programmatic identifier (ProgID)](/windows/win32/shell/fa-progids) values that describes the application, component, and version of each desktop application from which you want to inherit file associations. |

## Requirements

| Item | Value |
|-|-|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities/3` |
