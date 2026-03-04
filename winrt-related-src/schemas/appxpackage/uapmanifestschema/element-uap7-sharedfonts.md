---
title: uap7:SharedFonts
description: Contains the locations of shared fonts to be used with the app. This version of the extension is in the uap7 namespace.
ms.date: 09/11/2020
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Extensions, uap7:Extension, uap7:SharedFonts]
---

# uap7:SharedFonts

Contains the locations of custom fonts to be shared with other apps. For more information about this extension, see [this article](/windows/apps/desktop/modernize/desktop-to-uwp-extensions#share-fonts-with-other-windows-applications).

> [!NOTE]
> Before you can submit an app that uses this extension to the Store, you must first obtain approval from the Store team. To obtain approval, go to [https://aka.ms/storesupport](https://aka.ms/storesupport), click **Contact us**, and choose options relevant to submitting apps to the dashboard. This approval process helps to ensure that there are no conflicts between fonts installed by your app and fonts that are installed with the OS. If you do not obtain approval, you will receive an error similar to the following when you submit your app: "Package acceptance validation error: You can't use extension windows.sharedFonts with this account. Contact our support team if you'd like to request permissions to use this extension."

## Element hierarchy

**[`<Package>`](element-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap7:Extension>`](element-uap7-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap7:SharedFonts>`**  

## Syntax

```xml
<uap7:SharedFonts >

 <!-- Child elements -->
 uap4:Font

</uap7:SharedFonts>
```

## Attrbutes and elements

### Attributes

None

### Child elements

| Child element | Description |
|-|-|
| **uap4:Font** | Specifies the font file packaged with the app. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap7:Extension](element-uap7-extension.md) | Declares an extensibility point for the app. |

## Remarks

The **sharedFonts** element defined in **uap7:Extension** is a descendent of [Package](element-package.md) and is associated with the package identity, regardless of how many apps the package contains. This includes packages that contain no applications at all. When the application is installed, the user is not presented with the system font installation UI.

The **sharedFonts** element defined in **uap4:Extension** provides similar functionality, but is a descendent of [Application](element-application.md) and is associated to a specific application's identity. When the application is installed, the user is presented with the system font installation UI.

For both versions of this extension, the fonts are installed per-user.

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/7` |
| **Minimum OS Version** | Windows 10 version 1809 (Build 17763) |
