---
description: Identifies the device family that a package targets. (descendant of Packages).
Search.Product: eADQiWindows 10XVcnh
title: TargetDeviceFamily (Bundle schema, descendant of Packages)
ms.assetid: 445e7de7-e778-4666-b099-3d7f6f0125c7


keywords: windows 10, uwp, schema, bundle manifest


ms.topic: reference
ms.date: 04/05/2017
---

# TargetDeviceFamily (Bundle schema, descendant of Packages)

Identifies the device family that a package targets. For more info about device families, see [Programming with extension SDKs](/uwp/extension-sdks/device-families-overview).

## Element hierarchy

<dl>
<dt><a href="element-bundle.md">&lt;Bundle&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-packages.md">&lt;Packages&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-dependencies.md">&lt;Dependencies&gt;</a></dt>
<dd><b>&lt;TargetDeviceFamily&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

```xml
<TargetDeviceFamily
    Name = 'An alphanumeric string that can contain period and dash characters.'
    MinVersion = 'A version string in quad notation ("Major.Minor.Build.Revision"), where Major cannot be 0.'
    MaxVersionTested = 'A version string in quad notation ("Major.Minor.Build.Revision"), where Major cannot be 0.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the device family that your app is targeting.  | An alphanumeric string that can contain period and dash characters. | Yes |  |
| **MinVersion** | The minimum version of the device family that your app is targeting. Used for applicability at deployment time. If the device family version of the system is lower than *MinVersion*, then the app is not considered applicable. | A version string in quad notation (`Major.Minor.Build.Revision`), where `Major` cannot be `0`. | Yes |  |
| **MaxVersionTested** | The maximum version of the device family that your app is targeting that you have tested it against. This is used at runtime to determine the effective process space for quirks. | A version string in quad notation (`Major.Minor.Build.Revision`), where `Major` cannot be `0`. | Yes |  |

### Child elements

None.

### Parent Elements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Parent Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="element-resources.md">Dependencies</a> </td>
<td><p>Declares dependencies that will be installed if required.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

|          | Value        |
|----------|--------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2018/bundle` |

 

 
