---
description: Declares an app extensibility point of type windows.webAccountProvider.
Search.Product: eADQiWindows 10XVcnh
title: uap:WebAccountProvider (Windows 10)
ms.assetid: 9e38d699-4a07-46ac-88d4-70109fbaa892


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# uap:WebAccountProvider (Windows 10)


Declares an app extensibility point of type **windows.webAccountProvider**.

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
<dd><b>&lt;uap:WebAccountProvider&gt;</b></dd>
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
<WebAccountProvider Url                  = A string between 1 and 32767 characters in length in the form of a valid web url.
                        BackgroundEntryPoint = A string between 1 and 256 characters in length, representing the  task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type.
If EntryPoint is not specified, the EntryPoint defined for the app is used instead.
 >

  <!-- Child elements -->
  uap:ManagedUrls?

</uap:WebAccountProvider>
```

### Key

`?`   optional (zero or one)

## Attributes and Elements


### Attributes

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
<th>Data type</th>
<th>Required</th>
<th>Default value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>BackgroundEntryPoint</strong></td>
<td><p>Entry Point for UI-less get token request.</p></td>
<td>A string between 1 and 256 characters in length, representing the task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. If EntryPoint is not specified, the EntryPoint defined for the app is used instead.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Url</strong></td>
<td><p>The Web Account provider identifier (URL). Should be a valid HTTPS URL. Used to uniquely identify the provider when called from an app.</p></td>
<td>A string between 1 and 32767 characters in length in the form of a valid web url.</td>
<td>Yes</td>
<td></td>
</tr>
</tbody>
</table>

 

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
<td><a href="element-uap-managedurls.md">uap:ManagedUrls</a> </td>
<td><p>Provides support for multiple URLs. Allows plugins to specify multiple URLs to which they may send cookies.</p></td>
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
<td><a href="element-uap-extension.md">uap:Extension</a> </td>
<td><p>Declares an extensibility point for the app.</p></td>
</tr>
</tbody>
</table>

 

## Examples

```XML
    <Extension Category="windows.webAccountProvider">
        <WebAccountProvider Url="https://login.live.com"
            BackgroundEntryPoint="MSA.WebAccountProviderTask"/>
    </Extension>
```

## Requirements

|   |   |
|--|--|
| Namespace | `	http://schemas.microsoft.com/appx/manifest/uap/windows10` |


 

 



