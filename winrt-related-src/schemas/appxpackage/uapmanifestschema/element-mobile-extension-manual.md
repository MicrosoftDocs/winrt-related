---
Description: Declares an extensibility point for the app.
Search.Product: eADQiWindows 10XVcnh
title: mobile:Extension (Windows 10)
ms.assetid: 0f9f4bee-3a63-4383-86db-a555ca4ccad6
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 04/05/2017
---

# mobile:Extension (Windows 10)


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
<dd><b>&lt;mobile:Extension&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax


```
<mobile:Extension Category = "windows.aowApp" | "windows.mobileMultiScreenProperties" | "windows.communicationBlockingProvider" | "windows.phoneCallOriginProvider"
               Executable?    = A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn&#39;t specified, the EntryPoint defined for the app is used.
               EntryPoint?    = A string between 1 and 256 characters in length, representing the  task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type.
If EntryPoint is not specified, the EntryPoint defined for the app is used instead.

               RuntimeType?   = A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, |, ?, or *.
               StartPage?     = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.
               ResourceGroup? = An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. >

  <!-- Child elements -->
  ( mobile:AowApp
  | mobile:MobileMultiScreenProperties
  )?

</mobile:Extension>
```

**Key**

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
<li>windows.aowApp</li>
<li>windows.mobileMultiScreenProperties</li>
<li>windows.communicationBlockingProvider</li>
<li>windows.phoneCallOriginProvider</li>
</ul></td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>EntryPoint</strong></td>
<td>The activatable class ID.</td>
<td>A string between 1 and 256 characters in length, representing the task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. If EntryPoint is not specified, the EntryPoint defined for the app is used instead.</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Executable</strong></td>
<td>The default launch executable.</td>
<td>A string between 1 and 256 characters in length that must end with &quot;.exe&quot; and cannot contain these characters: &lt;, &gt;, :, &quot;, |, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used. If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used.</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>ResourceGroup</strong></td>
<td>A tag that you can use to group extension activations together for resource management purposes (for example, CPU and memory). The value you can set ResourceGroup is free-form and flexible. See [<strong>Application@ResourceGroup</strong>](element-application.md).</td>
<td>An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>RuntimeType</strong></td>
<td>The runtime provider. This attribute is used typically when there are mixed frameworks in an app.</td>
<td>A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: &lt;, &gt;, :, &quot;, /, \, |, ?, or *.</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>StartPage</strong></td>
<td>The web page that handles the extensibility point.</td>
<td>A string between 1 and 256 characters in length that cannot contain these characters: &lt;, &gt;, :, &quot;, |, ?, or *.</td>
<td>No</td>
<td></td>
</tr>
</tbody>
</table>

 

**Child Elements**

| Child Element                                                                                   | Description                                                                          |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [**mobile:AowApp**](element-mobile-aowapp-manual.md)                                           | Declares an app extensibility point of type **windows.aowApp**.                      |
| [**mobile:MobileMultiScreenProperties**](element-mobile-mobilemultiscreenproperties-manual.md) | Declares an app extensibility point of type **windows.MobileMultiScreenProperties**. |

 

**Parent Elements**

| Parent Element                                                               | Description                                           |
|------------------------------------------------------------------------------|-------------------------------------------------------|
| [**Extensions (type: CT_ApplicationExtensions)**](element-1-extensions.md) | Defines one or more extensibility points for the app. |

 

## Examples


The following example shows how to block your mobile app from being displayed on a connected display. This markup will cause your app's tile to be disabled on the connected display’s Start menu.

```XML
                    
<Package ...
         xmlns:mobile="http://schemas.microsoft.com/appx/manifest/mobile/windows10"
         IgnorableNamespaces="... mobile">
    <Applications>
        <Application>
            <Extensions>
                <mobile:Extension Category="windows.mobileMultiScreenProperties">
                    <mobile:MobileMultiScreenProperties RestrictToInternalScreen="true"/>
                </mobile:Extension>
            </Extensions>
        </Application>
    </Applications>
</Package>
                
```

## Requirements


|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | http://schemas.microsoft.com/appx/manifest/mobile/windows10 |

 

 

 



