---
Description: Represents one or more apps that comprise the package.
Search.Product: eADQiWindows 10XVcnh
title: Applications
ms.assetid: ad9e07fc-ba58-4465-b3fa-b330ba149f92


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# Applications


Represents one or more apps that comprise the package.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd><b>&lt;Applications&gt;</b></dd>
</dl>

## Syntax

``` syntax
<Applications>

  <!-- Child elements -->
  Application{1,100}

</Applications>
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
<td><a href="element-application.md">Application</a> </td>
<td><p>Represents an app that comprises part of or all of the functionality delivered in the package.</p></td>
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
<td><a href="element-package.md">Package</a> </td>
<td><p>Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

You can use the **Applications** element to specify one or more apps for the package. Note that although each package can contain one or more apps, packages that contain multiple apps won't pass the Microsoft Store certification process.

## Examples

The following example is taken from the package manifest of one of the SDK samples.

```XML
<Applications>
  <Application Id="App" StartPage="default.html">
    <VisualElements DisplayName="Assocation launching sample" 
         Logo="images\squareTile-sdk.png" SmallLogo="images\smallTile-sdk.png" 
         Description="SDK sample" 
         ForegroundText="dark" BackgroundColor="#FFFFFF" ToastCapable="false">
      <DefaultTile ShowName="allLogos" />
      <SplashScreen BackgroundColor="white" Image="images\splash-sdk.png" />
    </VisualElements>
    <Extensions>
      <Extension Category="windows.fileTypeAssociation">
        <FileTypeAssociation Name=".alsdkjs">
          <SupportedFileTypes>
            <FileType>.alsdkjs</FileType>
          </SupportedFileTypes>
        </FileTypeAssociation>
      </Extension>
      <Extension Category="windows.protocol">
        <Protocol Name="alsdkjs" />
      </Extension>
    </Extensions>
  </Application>
</Applications>
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
<td><pre>http://schemas.microsoft.com/appx/2010/manifest</pre></td>
</tr>
</tbody>
</table>

 

 



