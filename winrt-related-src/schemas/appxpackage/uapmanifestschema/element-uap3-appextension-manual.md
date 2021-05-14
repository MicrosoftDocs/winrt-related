---
description: Declares an app extensibility point of type windows.appExtension.
Search.Product: eADQiWindows 10XVcnh
title: uap3:AppExtension
ms.assetid: 88e4b56d-e2c2-4782-bedd-eae33d069c2c


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# uap3:AppExtension


Declares an app extensibility point of type **windows.appExtension**. This element indicates which categories of extensions the app intends to consume and/or host.

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
<dt><a href="element-uap3-extension-manual.md">&lt;uap3:Extension&gt;</a></dt>
<dd><b>&lt;uap3:AppExtension&gt;</b></dd>
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


```
<uap3:AppExtension Name         = A string between 2 and 255 characters in length that
                                  consists of alphanumeric, period (except for the first
                                  character), and dash characters only.
                   Id           = A string between 2 and 39 characters in length that
                                  consists of alphanumeric, period (except for the first
                                  character), and dash characters only.
                   PublicFolder = A string between 1 and 256 characters in length that
                                  cannot contain these characters: <, >, :, ", |, ?, or *.
                   DisplayName  = A string between 1 and 256 characters in length.
                   Description? = A string between 1 and 2048 characters in length that
                                  cannot include characters such as tabs, carriage returns,
                                  and line feeds. >
  <!-- Child elements -->
  uap3:Properties?
</uap3:AppExtension>
```

### Key
`?` optional (zero or one)

## Attributes and Elements


**Attributes**

| Attribute        | Description                                                                                                         | Data type                                                                                                                                        | Required | Default value |
|------------------|---------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|----------|---------------|
| **Description**  | The description of the app extension.                                                                               | A string between 1 and 2048 characters in length that cannot include characters such as tabs, carriage returns, and line feeds.                  | No       |               |
| **DisplayName**  | A friendly name for the app extension that can be displayed to users.                                               | A string between 1 and 256 characters in length.                                                                                                 | Yes      |               |
| **Id**           | The entry point by which the host app accesses the extension category instance, if there are multiple entry points. | A string between 2 and 39 characters in length that consists of alphanumeric, period (except for the first character), and dash characters only. | Yes      |               |
| **Name**         | The type of extension that the app intends to consume and/or host.                                                  | A string between 2 and 255 characters in length that consists of alphanumeric, period (except for the first character), and dash characters only. | Yes      |               |
| **PublicFolder** | The folder that the instance declares as the location where a host can have read access to files through a broker.  | A string between 1 and 256 characters in length that cannot contain these characters: &lt;, &gt;, :, ", \|, ?, or \*.                            | Yes      |               |

 

**Child Elements**

| Child Element                                            | Description                                                                                                                                                                          |
|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**uap3:Properties**](elemnt-uap3-properties-manual.md) | Contains opaque XML that represents custom, extension-specific information that is simply stored and not read by the operating system. The information is only read by the host app. |

 

**Parent Elements**

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
<td><a href="element-uap3-extension-manual.md"><strong>uap3:Extension</strong></a> </td>
<td><p>Declares an extensibility point for the app.</p></td>
</tr>
</tbody>
</table>

 

## Examples


The following example indicates that the app hosts or consumes the low-performance browser extension

```XML
<Package ...
         xmlns:uap3="http://schemas.microsoft.com/appx/manifest/uap/windows10/3"  
         IgnorableNamespaces="... uap3">
    <Applications>
        <Application>
            <Extensions>
                <uap3:Extension Category="windows.appExtension">  
                    <uap3:AppExtension Name="com.microsoft.browser.ext"
                                       Id="Extension.Low.Performance"
                                       PublicFolder="public\lowperf"
                                       DisplayName="Low Performance Extension"/>  
                </uap3:Extension>  
              </Extensions>
        </Application>
    </Applications>
</Package>
```

## Requirements


|               | Value                                                       |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |

 

 

 
