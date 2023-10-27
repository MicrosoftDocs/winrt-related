---
ms.assetid: 5872b49b-5572-4198-8765-775c7a5a36fc
title: rescap3:MigrationProgIds (child of uap:Protocol)
description: "Learn more about: rescap3:MigrationProgIds"
ms.date: 04/05/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# rescap3:MigrationProgIds (child of uap:Protocol)

Contains Migration Prog Ids for protocols and file type associations.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:Extension\>](element-uap-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:Protocol\>](element-uap-protocol.md)

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

| Child Element | Description |
|-|-|
| [MigrationProgId](element-uap-protocol-migrationprogid.md) | Contains a migration Prog Id string for protocols and file type associations. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap:Protocol](element-uap-protocol.md) | Declares an app extensibility point of type *windows.protocol*. A URI association indicates that the app is registered to handle URIs with the specified scheme. |

## Requirements

| Item | Value |
|-|-|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities/3` |
| Minimum OS Version | Windows 10 version 1511 (Build 10586) |
