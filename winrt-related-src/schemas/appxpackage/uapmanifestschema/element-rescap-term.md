---
title: rescap:Term
description: Registers a search term for a settings app.
ms.date: 03/14/2022
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, extension
no-loc: [Package, Applications, Application, Extensions, rescap:Extension, rescap:SearchTerms]
---

# rescap:Term

Registers a search term for a settings app.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-1-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<rescap:Extension>`](element-rescap-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<rescap:SearchTerms>`**  

## Syntax

```xml
<rescap:Term>

  A string specifying a search term to be associated with the settings app.

</rescap:Term>
```


## Attributes and elements

### Attributes

None.

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [rescap:SearchTerms](element-rescap-searchterms.md) | Registers one or more search terms for a settings app. |

### Remarks

For information about creating and registering a settings app, see [Create a partner settings app](/windows-hardware/drivers/partnerapps/create-a-system-settings-application).

## Requirements

| Item | Value |
|--|--|
| **rescap** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |
