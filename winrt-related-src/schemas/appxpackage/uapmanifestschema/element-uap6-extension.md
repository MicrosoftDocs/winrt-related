---

title: uap6:Extension
description: Declares an extensibility point for the app.

ms.date: 04/10/2018
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, extension 
---

# uap6:Extension

## Description
Declares an extensibility point for the app.

## Element Hierarchy
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
<dd><b>&lt;uap6:Extension&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>


## Syntax
```syntax
<uap6:Extension Category       = "windows.barcodeScannerProvider" | "windows.localExperiencePack"
                   Executable?    = A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used.
                   EntryPoint?    = A string between 1 and 256 characters in length, representing the  task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. If EntryPoint is not specified, the EntryPoint defined for the app is used instead.
                   RuntimeType?   = A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, |, ?, or *.
                   StartPage?     = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *. 
                   ResourceGroup? = An alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. >

  <!-- Child elements -->
  ( uap6:BarcodeScannerProvider
  | uap6:LocalExperiencePack )?

</uap6:Extension>
```

### Key
`?` optional (zero or one)

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Category | The category of the extension. | One of the following:<ul><li>windows.barcodeScannerProvider</li><li>windows.localExperiencePack</li></ul> | Yes |
| Executable | The default launch executable. | A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", &#124;, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used. | No |
| EntryPoint | The activatable class ID. | A string between 1 and 256 characters in length, representing the task handling the extension. This is normally the fully namespace-qualified name of a Windows Runtime type. If EntryPoint is not specified, the EntryPoint defined for the app is used instead. | No |
| RuntimeType | The runtime provider. This attribute is used typically when there are mixed frameworks in an app. | A string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, &#124;, ?, or *. | No |
| StartPage | The web page that handles the extensibility point. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |


## Child Elements

| Child Element | Description |
|---------------|-------------|
| [BarcodeScannerProvider](element-uap6-barcodescannerprovider.md) | Used for enabling the support of a barcode scanner. |  
| [LocalExperiencePack](element-uap6-localexperiencepack.md) | This extension provides a means to deliver translated app resources. | 


## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10/6</p></td>
</tr>
</tbody>
</table>