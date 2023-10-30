---
description: Declares that the current package is a modification package for an enterprise application.
title: rescap6:ModificationPackage
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/19/2019
ms.custom: 19H1
---

# rescap6:ModificationPackage

Declares that the current package is a [modification package](/windows/msix/modification-packages) for an enterprise application.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Properties\>](element-properties.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<rescap6:ModificationPackage\>**

## Syntax

``` xml
<rescap6:ModificationPackage>true</rescap6:ModificationPackage>
```

## Attributes and elements

### Attributes

None.

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [Properties](element-properties.md) | Defines additional metadata about the package including attributes that describe how the package appears to users. |  

## Remarks

This element represents a restricted property that is only supported in [optional packages](/windows/uwp/packaging/optional-packages). This element is currently intended to be used only for enterprise applications. We don't recommend that you declare this capability in applications that you submit to the Microsoft Store. In most cases, the use of this element won't be approved.

For more information, see [Modification packages](/windows/msix/modification-packages).

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities/6` |
| **Minimum OS Version** | Windows 10 version 1903 (Build 18362) |
