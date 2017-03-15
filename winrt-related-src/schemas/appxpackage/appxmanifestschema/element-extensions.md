---
Description: 'Extensions (type: CT\_PackageExtensions)'
MS-HAID: AppxManifestSchema.element\_Extensions
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: 'Extensions (type: CT\_PackageExtensions)'
ms.assetid: 837ae066-b590-4f58-b552-2e9d608f0fac
author: laurenhughes
ms.author: lahugh
keywords: windows 10
---

# Extensions (type: CT\_PackageExtensions)


Defines one or more extensibility points for the package.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd><b>&lt;Extensions&gt;</b></dd>
</dl>

## Syntax

``` syntax
<Extensions>

  <!-- Child elements -->
  Extension{1,10000}

</Extensions>
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
<td>[Extension (in type: CT_PackageExtensions)](element-extension.md)</td>
<td><p>Declares an extensibility point for the package.</p></td>
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

 

## Related elements


The following elements have the same name as this one, but different content or attributes:

-   **[Extensions (type: CT\_ApplicationExtensions)](element-1-extensions.md)**

## Remarks

Extensibility points are a mechanism by which an app can add functionality in a manner defined by the operating system. An example of a package extensibility point is the ability to specify a dynamic-link library or executable that contains activatable classes that your code uses.

## Examples

The following example is taken from the package manifest of one of the SDK samples.

```XML
<Package>
  <Extensions>
    <Extension Category="windows.activatableClass.proxyStub">
      <ProxyStub ClassId="332fd2f1-1c69-4c91-949e-4bb67a85bdc5">
        <Path>Microsoft.Samples.DllServerAuthoring.Proxies.dll</Path>
        <Interface Name="IToaster" InterfaceId="6a112353-4f87-4460-a908-2944e92686f3" />
        <Interface Name="IToast" InterfaceId="699b1394-3ceb-4a14-ae23-efec518b088b" />
        <Interface Name="IAppliance" InterfaceId="332fd2f1-1c69-4c91-949e-4bb67a85bdc5" />
      </ProxyStub>
    </Extension>
    <Extension Category="windows.activatableClass.inProcessServer">
      <InProcessServer>
        <Path>Microsoft.Samples.DllServerAuthoring.dll</Path>
        <ActivatableClass ActivatableClassId="Microsoft.Samples.DllServerAuthoring.Toaster" ThreadingModel="both" />
      </InProcessServer>
    </Extension>
  </Extensions>
</Package>

```

## See also


**Concepts**
[App contracts and extensions](https://msdn.microsoft.com/library/windows/apps/hh464906)

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

 

 



