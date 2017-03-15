---
Description: Capabilities
MS-HAID: AppxManifestSchema.element\_Capabilities
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: Capabilities
ms.assetid: 508b9a46-3dd4-4bce-875b-fb7cadadceb1
author: laurenhughes
ms.author: lahugh
keywords: windows 10
---

# Capabilities


Declares the access to protected user resources that the package requires.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd><b>&lt;Capabilities&gt;</b></dd>
</dl>

## Syntax

``` syntax
<Capabilities>

  <!-- Child elements -->
  Capability{0,10},
  DeviceCapability{0,100}

</Capabilities>
```

### Key

`{}`   specific range of occurrences

## Attributes and Elements


### Attributes

None.

### Child Elements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Child Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[Capability](element-capability.md)</td>
<td><p>Declares a capability required by a package.</p></td>
</tr>
<tr class="even">
<td>[DeviceCapability](element-devicecapability.md)</td>
<td><p>Declares a device capability required by a package.</p></td>
</tr>
</tbody>
</table>

 

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
<td>[Package](element-package.md)</td>
<td><p>Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

If you do not explicitly declare the capabilities required for your app to access user resources, your app cannot access that resource. However, even if you declare a capability, your app still won't have access to the user resource if it does not exist on the system or there are other security policies in place that limit access to the resource.

## Examples

Here's an example **Capabilities** node that declares 3 capabilities.

```XML
<Capabilities>
  <Capability Name="internetClient"/>
  <Capability Name="musicLibrary"/>
  <Capability Name="videosLibrary"/>
</Capabilities>
```

## See also


[App capability declarations](https://msdn.microsoft.com/library/windows/apps/hh464936)

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/2010/manifest</p></td>
</tr>
</tbody>
</table>

 

 



