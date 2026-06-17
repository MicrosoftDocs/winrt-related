---
title: uap7:SharedFonts
description: Contains the locations of shared fonts to be used with the app. This version of the extension is in the uap7 namespace.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, uap7:Extension, uap7:SharedFonts]
---

# uap7:SharedFonts

Contains the locations of custom fonts to be shared with other apps. For more information about this extension, see [Share fonts with other Windows applications](/windows/apps/desktop/modernize/desktop-to-uwp-extensions#share-fonts-with-other-windows-applications).

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap7:Extension>`](element-uap7-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap7:SharedFonts>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap7:Extension>`](element-uap7-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap7:SharedFonts>`**  

## Syntax

```xml
<uap7:SharedFonts>

  <!-- Child elements -->
  uap7:Font{1,unbounded}

</uap7:SharedFonts>
```

### Key

`{}` specific range of occurrences

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| **uap4:Font** | Specifies the font file packaged with the app. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap7:Extension](element-uap7-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/7` |
| **Minimum OS Version** | Windows 10 version 1809 (Build 17763) |

## Remarks

> [!NOTE]
> Before you can submit an app that uses this extension to the Store, you must first obtain approval from the Store team. To obtain approval, go to [https://aka.ms/storesupport](https://aka.ms/storesupport), click **Contact us**, and choose options relevant to submitting apps to the dashboard. This approval process helps to ensure that there are no conflicts between fonts installed by your app and fonts that are installed with the OS. If you do not obtain approval, you will receive an error similar to the following when you submit your app: "Package acceptance validation error: You can't use extension windows.sharedFonts with this account. Contact our support team if you'd like to request permissions to use this extension."

The **sharedFonts** element defined in **uap7:Extension** is a descendent of [Package](element-f-package.md) and is associated with the package identity, regardless of how many apps the package contains. This includes packages that contain no applications at all.

The **sharedFonts** element defined in **uap4:Extension** provides similar functionality, but is a descendent of [Application](element-f-application.md) and is associated to a specific application's identity.

For both versions of this extension, the fonts are installed per-user.

## Examples

<!-- Author content goes here -->