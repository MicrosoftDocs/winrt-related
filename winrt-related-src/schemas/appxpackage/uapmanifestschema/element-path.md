---
Description: Path (in InProcessServer) (Windows 10)
MS-HAID: UapManifestSchema.element\_Path
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: Path (in InProcessServer) (Windows 10)
ms.assetid: 337dd035-774d-40fb-8da1-7af11dbb4a35
author: laurenhughes
ms.author: lahugh
keywords: windows 10
---

# Path (in InProcessServer) (Windows 10)


The path to the DLL.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extension.md">&lt;Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-inprocessserver.md">&lt;InProcessServer&gt;</a></dt>
<dd><b>&lt;Path&gt;</b></dd>
</dl>
<dl>
<dt><a href="element-proxystub.md">&lt;ProxyStub&gt;</a></dt>
<dd><b>&lt;Path&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<Path>

  A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.

</Path>
```

## Attributes and Elements


### Attributes

None.

### Child Elements

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
<td>[InProcessServer](element-inprocessserver.md)</td>
<td><p>Declares a package extensibility point of type <strong>windows.activatableClass.inProcessServer</strong>. The app uses a dynamic link library (DLL) that exposes one or more activatable classes.</p></td>
</tr>
<tr class="even">
<td>[ProxyStub](element-proxystub.md)</td>
<td><p>Declares a package extensibility point of type <strong>windows.activatableClass.proxyStub</strong>. A proxy can be composed of one or more interfaces.</p></td>
</tr>
</tbody>
</table>

 

## Related elements


The following elements have the same name as this one, but different content or attributes:

-   **[Path (type: ST\_Executable)](element-1-path.md)**

## Examples

```XML
<Extension Category="windows.activatableClass.inProcessServer">
      <InProcessServer>
        <Path>Microsoft.Samples.DllServerAuthoring.dll</Path>
        <ActivatableClass ActivatableClassId="Microsoft.Samples.DllServerAuthoring.Toaster" ThreadingModel="both" />
      </InProcessServer>
</Extension>
```

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/foundation/windows10</p></td>
</tr>
</tbody>
</table>

 

 



