---
description: Indicates whether Windows will enforce runtime package integrity checks on the package.
title: tbd:TrustedLaunch
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 02/06/2020
---

# uap10:PackageIntegrity

Specifies that Trusted Launch is enabled, which restricts the set of processes that can be launched under a package's identity.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Properties\>](element-properties.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<tbd:TrustedLaunch\>**

## Syntax

```xml
<tbd:TrustedLaunch>

  <!-- a string value of either "true" or "false" -->

</uap10:TrustedLaunch>
```


## Attributes and elements

### Attributes

None.

### Child elements

None

### Parent elements

| Parent element | Description |
|-|-|
| [Properties](element-properties.md) | Defines additional metadata about the package including attributes that describe how the package behaves. |

## Remarks

For Trusted Launch to be enabled, you must set the contents **TrustedLaunch** to "true" and you must also include a [uap10:PackageIntegrity](element-uap10-packageintegrity.md) element and its child [uap10:content](element-uap10-content.md) element, with the **Enforcement** attribute set to "on".

Enabling Trusted Launch will cause SignTool to generate a catalog file containing all of the packaged executable files within the new package. Only executables within the signed catalog file are allowed to run under the package's identity.

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/trustedlaunch/windows10` |
| **Minimum OS Version** | Windows 10 version 26100 |
