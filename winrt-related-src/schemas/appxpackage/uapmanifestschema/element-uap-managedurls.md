---
Description: Provides support for multiple URLs.
Search.Product: eADQiWindows 10XVcnh
title: uap:ManagedUrls (Windows 10)
ms.assetid: 9b4709ea-cce3-472c-a799-96039241fd0b
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# uap:ManagedUrls (Windows 10)


Provides support for multiple URLs. Allows plugins to specify multiple URLs to which they may send cookies.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap-extension.md">&lt;uap:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap-webaccountprovider.md">&lt;uap:WebAccountProvider&gt;</a></dt>
<dd><b>&lt;uap:ManagedUrls&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<ManagedUrls>

  <!-- Child elements -->
  uap:Url{1,200}

</uap:ManagedUrls>
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
<td>[uap:Url](element-uap-url.md)</td>
<td><p>Specifies a URL to which a plugin may send cookies. Need only be a valid URI; not necessarily a URL.</p></td>
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
<td>[uap:WebAccountProvider](element-uap-webaccountprovider.md)</td>
<td><p>Declares an app extensibility point of type <strong>windows.webAccountProvider</strong>.</p></td>
</tr>
</tbody>
</table>

 

## Examples

```XML
    <Extension Category="windows.webAccountProvider">
        <WebAccountProvider Url="https://login.live.com"
            BackgroundEntryPoint="MSA.WebAccountProviderTask">
            <uap:ManagedUrls>
                <uap:Url>https://login.windows.cn</uap:Url>
                <uap:Url>https://login.windows.us</uap:Url>
            </uap:ManagedUrls>
        </WebAccountProvider>
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
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10</p></td>
</tr>
</tbody>
</table>

 

 



