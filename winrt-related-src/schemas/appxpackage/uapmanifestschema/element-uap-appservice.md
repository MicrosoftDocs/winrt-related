---
Description: Declares an app extensibility point of type windows.appService.
Search.Product: eADQiWindows 10XVcnh
title: uap:AppService (Windows 10)
ms.assetid: 53420864-d8b4-4f30-bb74-5148d89be5f1
author: mcleanbyron
ms.author: mcleans
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# uap:AppService (Windows 10)


Declares an app extensibility point of type **windows.appService**. Application Contracts are a way for an app to invoke a background task belonging to another app; or for a background task invoked to service an app contract a way to communicate with its caller.

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
<dd><b>&lt;uap:AppService&gt;</b></dd>
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
<AppService Name        = A string between 2 and 39 characters in length that consists of alphanumeric, period (except for the first character), and dash characters only.
            ServerName? = An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. 
            uap4:SupportsMultipleInstances = Boolean. />
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
<td><strong>Name</strong></td>
<td><p>The service name (used to match the caller of the Application Contract with the provider).</p></td>
<td>A string between 2 and 39 characters in length that consists of alphanumeric, period (except for the first character), and dash characters only.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>ServerName</strong></td>
<td><p>The COM server to be instantiated to satisfy the contract activation (ensures that only one instance of the server exists at runtime). This is an optional attribute that is only used for PPLE host processes.</p></td>
<td>An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>uap4:SupportsMultipleInstances</strong></td>
<td><p>Supports multiple, separate instances of an app service.</p></td>
<td>Boolean.</td>
<td>No</td>
<td></td>
</tr>
</tbody>
</table>

 

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
<td><a href="element-uap-extension.md">uap:Extension</a> </td>
<td><p>Declares an extensibility point for the app.</p></td>
</tr>
</tbody>
</table>

 

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

 

 



