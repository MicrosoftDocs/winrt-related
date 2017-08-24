---
Description: Contains the driver constraint information for a UWP app.
title: uap5:DriverDependency
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest, driver dependency
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 8/25/17
---

# uap5:DriverDependency
Contains the driver constraint information for a UWP app. If `DriverDependency` is used, the specified driver must be present for the app to load.

> [!NOTE] 
> This is available in current [Windows 10 Insider Preview](https://insider.windows.com/) builds only.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-dependencies.md">&lt;Dependencies&gt;</a></dt>
<dd><b>&lt;uap5:DriverDependency&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<uap5:DriverDependency>
  <!-- Child elements -->
  uap5:DriverConstraint{1,1000}
</uap5:DriverDependency>
```

## Attributes and Elements
### Attributes
None

### Child Elements
| Child Element | Description |
|---------------|-------------|
| [DriverConstraint](element-uap5-DriverConstraint.md) | Specifies the details of a driver paired with a UWP app. |

## Remarks
If you are pairing a driver with a UWP app, at least one `DriverDependency` must be met for the app to load. For a `DriverDependency` to be met, all its [`DriverConstraint`](element-uap5-DriverConstraint.md) elements must be met. 

See [Pairing a driver with a Universal Windows Platform (UWP) app](/windows-hardware/drivers/install/pairing-app-and-driver-versions)

## Examples
See [uap5:DriverConstraint](element-uap5-DriverConstraint.md) for an example. 

## Requirements
> [!NOTE] 
> This is available in current [Windows 10 Insider Preview](https://insider.windows.com/) builds only.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10/5</p></td>
</tr>
</tbody>
</table>

 

 



