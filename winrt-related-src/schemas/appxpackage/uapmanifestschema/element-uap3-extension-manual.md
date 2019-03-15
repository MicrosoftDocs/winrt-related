---
Description: Declares an extensibility point for the app.
Search.Product: eADQiWindows 10XVcnh
title: uap3:Extension (Windows 10)
ms.assetid: ed8f9296-0771-48ab-aecf-cca642e830c1
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# uap3:Extension (Windows 10)


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
<dd><b>&lt;uap3:Extension&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax


```
<uap3:Extension Category       = "windows.appointmentDataProvider" | 
                                 "windows.emailDataProvider" | 
                                 "windows.contactDataProvider" | 
                                 "windows.appUriHandler" | 
                                 "windows.appExtensionHost" | 
                                 "windows.appExtension"
                Executable?    = A string between 1 and 256 characters in length that must 
                                 end with ".exe" and cannot contain these characters: <, >, 
                                 :, ", |, ?, or *. It specifies the default executable for 
                                 the extension. If not specified, the executable defined 
                                 for the app is used.  If specified, the EntryPoint 
                                 property is also used. If that EntryPoint property isn&#39;t 
                                 specified, the EntryPoint defined for the app is used.
                EntryPoint?    = A string between 1 and 256 characters in length, 
                                 representing the  task handling the extension. This is 
                                 normally the fully namespace-qualified name of a 
                                 Windows Runtime type. If EntryPoint is not specified, 
                                 the EntryPoint defined for the app is used instead.
                RuntimeType?   = A string between 1 and 255 characters in length that 
                                 cannot start or end with a period or contain these 
                                 characters: <, >, :, ", /, \, |, ?, or *.
                StartPage?     = A string between 1 and 256 characters in length that 
                                 cannot contain these characters: <, >, :, ", |, ?, or *.
                ResourceGroup? = An alphanumeric string between 1 and 255 characters in 
                                 length. Must begin with an alphabetic character. >
  <!-- Child elements -->
  ( uap3:appointmentDataProvider
  | uap3:emailDataProvider
  | uap3:contactDataProvider
  | uap3:appUriHandler
  )?

</uap3:Extension>
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
<li>windows.appointmentDataProvider</li>
<li>windows.emailDataProvider</li>
<li>windows.contactDataProvider</li>
<li>windows.appUriHandler</li>
<li>windows.appExtensionHost</li>
<li>windows.appExtension</li>
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
<td>A tag that you can use to group extension activations together for resource management purposes (for example, CPU and memory). The value you can set ResourceGroup is free-form and flexible. See <a href="element-application.md"><strong>Application@ResourceGroup</strong></a> .</td>
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

| Child Element                                                                       | Description                                                                      |
|-------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [**uap3:AppointmentDataProvider**](element-uap3-appointmentdataprovider-manual.md) | Declares an app extensibility point of type **windows.appointmentDataProvider**. |
| [**uap3:EmailDataProvider**](element-uap3-emaildataprovider-manual.md)             | Declares an app extensibility point of type **windows.emailDataProvider**.       |
| [**uap3:ContactDataProvider**](element-uap3-contactdataprovider-manual.md)         | Declares an app extensibility point of type **windows.contactDataProvider**.     |
| [**uap3:AppUriHandler**](element-uap3-appurihandler-manual.md)                     | Declares an app extensibility point of type **windows.appUriHandler**.           |
| [**uap3:AppExtensionHost**](element-uap3-appextensionhost-manual.md)               | Declares an app extensibility point of type **windows.appExtensionHost**.        |
| [**uap3:AppExtension**](element-uap3-appextension-manual.md)                       | Declares an app extensibility point of type **windows.appExtension**.            |

 

**Parent Elements**

| Parent Element                                                               | Description                                           |
|------------------------------------------------------------------------------|-------------------------------------------------------|
| [**Extensions (type: CT_ApplicationExtensions)**](element-1-extensions.md) | Defines one or more extensibility points for the app. |

 

## Examples


```XML
<Package ...
         xmlns:uap3="http://schemas.microsoft.com/appx/manifest/uap/windows10/3"  
         IgnorableNamespaces="... uap3">
    <Applications>
        <Application>
            <Extensions>
                <uap3:Extension Category="windows.appointmentDataProvider" 
                                EntryPoint="UserDataProvider.AppointmentDataProviderTask">  
                    <uap3:AppointmentDataProvider ServerName="MyDataProvider.PPLE" />  
                </uap3:Extension>  
            </Extensions>
        </Application>
    </Applications>
</Package>
```

## Requirements


|               |                                                            |
|---------------|------------------------------------------------------------|
| **Namespace** | http://schemas.microsoft.com/appx/manifest/uap/windows10/3 |

 

 

 



