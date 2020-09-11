---
title: uap7:SharedFonts
description: Contains the locations of shared fonts to be used with the app. This version of the extension is in the uap7 namespace.
ms.date: 09/11/2020
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap7:SharedFonts

## Description

Contains the locations of custom fonts to be shared with other apps. For more information about this extension, see [this article](/windows/apps/desktop/modernize/desktop-to-uwp-extensions#share-fonts-with-other-windows-applications).

> [!NOTE]
> Before you can submit an app that uses this extension to the Store, you must first obtain approval from the Store team. To obtain approval, go to [https://aka.ms/storesupport](https://aka.ms/storesupport), click **Contact us**, and choose options relevant to submitting apps to the dashboard. This approval process helps to ensure that there are no conflicts between fonts installed by your app and fonts that are installed with the OS. If you do not obtain approval, you will receive an error similar to the following when you submit your app: "Package acceptance validation error: You can't use extension windows.sharedFonts with this account. Contact our support team if you'd like to request permissions to use this extension."

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap7-extension.md">&lt;uap7:Extension&gt;</a></dt>
<dd><b>&lt;uap7:SharedFonts&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>


## Syntax
```syntax
<uap7:SharedFonts >

 <!-- Child elements -->
 uap4:Font

</uap7:SharedFonts>
```

## Attrbutes and Elements

### Attributes
None

### Child Elements
| Child Element | Description |
|---------------|-------------|
| uap4:Font | Specifies the font file packaged with the app. |

## Requirements

|   |   |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/uap/windows10/7` |
