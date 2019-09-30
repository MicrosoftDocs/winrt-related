---
Description: Declares an extensibility point for the app.
Search.Product: eADQiWindows 10XVcnh
title: serverpreview:Extension
ms.assetid: c2f0aabe-bc7e-4c33-8f24-2cc848910666
author: mcleanbyron
ms.author: mcleans
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# serverpreview:Extension


Declares an extensibility point for the app.

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
<dd><b>&lt;serverpreview:EventProviders&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax


```
<serverpreview:Extension Category       = "windows.eventProviders" | 
                                          "windows.performanceProviders" | 
                                          "windows.iisModules"  |
                                          "windows.ntServices" |
                                          "windows.wmiProviders" >
  <!-- Child elements -->
  ( serverpreview:IisModules*
  | serverpreview:PerformanceProviders*
  | serverpreview:EventProviders*
  | serverpreview:NTServices*
  | serverpreview:WmiProviders*
  )*

</serverpreview:Extension>
```

**Key**

          \* optional (zero or more)

          ? optional (zero or one)

## Attributes and Elements


**Attributes**

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
<td><strong>Category</strong></td>
<td>The type of app extensibility point.</td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>windows.eventProviders</li>
<li>windows.performanceProvices</li>
<li>windows.iisModules</li>
<li>windows.ntServices</li>
<li>windows.wmiProviders</li>
</ul></td>
<td>Yes</td>
<td></td>
</tr>
</tbody>
</table>

 

**Child Elements**

| Child Element                                                                                   | Description                                                                   |
|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [**serverpreview:IisModules**](element-serverpreview-iismodules-manual.md)                     | Declares an app extensibility point of type **windows.iisModules**.           |
| [**serverpreview:PerformanceProviders**](element-serverpreview-performanceproviders-manual.md) | Declares an app extensibility point of type **windows.performanceProviders**. |
| [**serverPreview:EventProviders**](element-serverpreview-eventproviders-manual.md)             | Declares an app extensibility point of type **windows.eventProviders**.       |
| [**serverpreview:NTServices**](element-serverpreview-ntservices-manual.md)                     | Declares an app extensibility point of type **windows.ntServices**.           |
| [**serverpreview:WmiProviders**](element-serverpreview-wmiproviders-manual.md)                 | Declares an app extensibility point of type **windows.wmiProviders**.         |

 

**Parent Elements**

| Parent Element                                                               | Description                                           |
|------------------------------------------------------------------------------|-------------------------------------------------------|
| [**Extensions (type: CT_ApplicationExtensions)**](element-1-extensions.md) | Defines one or more extensibility points for the app. |

 

## Remarks


Set the **AppListEntry** attribute of the [**uap:VisualElements**](element-uap-visualelements.md) element for the application to "none" when you use server-specific app extensions.

## Examples


The following example identifies a performance counter to add to the server-specific app extensions.

```XML
<Package ...
         xmlns:serverpreview=http://schemas.microsoft.com/appx/manifest/serverpreview/windows10"  
         IgnorableNamespaces="... serverpreview">
    <Applications>
        <Application Id="TestPerformanceProvider">
            <uap:VisualElements AppListEntry="none" 
                                DisplayName="TestPerformanceProvider" 
                                Square150x150Logo="logo.png" 
                                Square44x44Logo="logo.png" 
                                Description="TestPerformanceProvider" 
                                BackgroundColor="#777777"/>
            <Extensions>
                <serverpreview:Extension Category="windows.performanceProviders">  
                    <serverpreview:PerformanceProviders>  
                        <serverpreview:PerformanceProvider Id="19b99d4e-deef-4de5-9fe8-5d53a01f79e0"
                                                           ManifestFile="Counters.xml"  
                                                           ResourceFile="PerfSample.exe" />  
                    </serverpreview:PerformanceProviders>  
                </serverpreview:Extension>  
            </Extensions>
        </Application>
    </Applications>
</Package>
```

## Requirements


|               |                                                                    |
|---------------|--------------------------------------------------------------------|
| **Namespace** | http://schemas.microsoft.com/appx/manifest/serverpreview/windows10 |

 

 

 



