---
title: ContentType
description: Setting the ContentType property on an element indicates that the element’s content is treated as a base64 encoding of the specified MIME type / content type and is indexed using the handler for that content type.
Search.Product: eADQiWindows 10XVcnh
ms.assetid: 74B75E30-8BF9-4443-941A-CA1E44A419CB

keywords: windows 10, uwp, schema


ms.topic: reference
ms.date: 04/05/2017
---

# ContentType

Setting this property on an element indicates that the element’s content is treated as a base64 encoding of the specified MIME type / content type and is indexed using the handler for that content type.

``` syntax
<element
    sc:ContentType= "application/hta" | "application/mac-binhex40" | "application/vnd.ms-xpsdocument"
        | "application/windows-appcontent+xml" | "application/x-compress" | "application/x-compressed" 
        | "application/x-gzip" | "application/x-jtx+xps" | "application/x-latex"
        | "application/x-mplayer2" | "application/x-ms-wmz" | "application/x-stuffit"
        | "application/x-tar" | "application/x-wmplayer" | "application/x-zip-compressed"
        | "application/xml" | "audio/aiff" | "audio/basic" | "audio/mid" | "audio/midi"
        | "audio/mp3" | "audio/mpeg" | "audio/mpegurl" | "audio/mpg" | "audio/wav"
        | "audio/x-aiff" | "audio/x-mid" | "audio/x-midi" | "audio/x-mp3" 
        | "audio/x-mpeg" | "audio/x-mpegurl" | "audio/x-mpg" | "audio/x-ms-wax" 
        | "audio/x-ms-wma" | "audio/x-wav" | "image/bmp" | image/gif" 
        | "image/jpeg" | "image/pjpeg" | "image/png" | "image/vnd.ms-photo"
        | "image/x-emf" | "image/x-icon" | "image/x-png" | "image/x-wmf"
        | "midi/mid" | "model/vnd.dwfx+xps" | "model/vnd.easmx+xps" 
        | "model/vnd.edrwx+xps" | "model/vnd.eprtx+xps" | "pkcs7-mime"
        | "text/css" | "text/html" | "text/plain" | "text/xml"
        | "video/avi" | "video/mpeg" | "video/mpg" | "video/msvideo" 
        | "video/quicktime" | "video/x-mpeg" | "video/x-mpeg2a" 
        | "video/x-ms-asf" | "video/x-ms-asf-plugin" | "video/x-ms-wm"
        | "video/x-ms-wmv" | "video/x-ms-wmx" | "video/x-ms-wvx"
        | "video/x-msvideo"
        xmlns:sc="http://schemas.microsoft.com/Search/2013/ApplicationContent">
</element>
```

## Data type


This attribute accepts one of the following values:

-   `application/hta`
-   `application/mac-binhex40`
-   `application/vnd.ms-xpsdocument`
-   `application/windows-appcontent+xml`
-   `application/x-compress`
-   `application/x-compressed`
-   `application/x-gzip`
-   `application/x-jtx+xps`
-   `application/x-latex`
-   `application/x-mplayer2`
-   `application/x-ms-wmz`
-   `application/x-stuffit`
-   `application/x-tar`
-   `application/x-wmplayer`
-   `application/x-zip-compressed`
-   `application/xml`
-   `audio/aiff`
-   `audio/basic`
-   `audio/mid`
-   `audio/midi`
-   `audio/mp3`
-   `audio/mpeg`
-   `audio/mpegurl`
-   `audio/mpg`
-   `audio/wav`
-   `audio/x-aiff`
-   `audio/x-mid`
-   `audio/x-midi`
-   `audio/x-mp3`
-   `audio/x-mpeg`
-   `audio/x-mpegurl`
-   `audio/x-mpg`
-   `audio/x-ms-wax`
-   `audio/x-ms-wma`
-   `audio/x-wav`
-   `image/bmp`
-   `image/gif`
-   `image/jpeg`
-   `image/pjpeg`
-   `image/png`
-   `image/vnd.ms-photo`
-   `image/x-emf`
-   `image/x-icon`
-   `image/x-png`
-   `image/x-wmf`
-   `midi/mid`
-   `model/vnd.dwfx+xps`
-   `model/vnd.easmx+xps`
-   `model/vnd.edrwx+xps`
-   `model/vnd.eprtx+xps`
-   `pkcs7-mime`
-   `text/css`
-   `text/html`
-   `text/plain`
-   `text/xml`
-   `video/avi`
-   `video/mpeg`
-   `video/mpg`
-   `video/msvideo`
-   `video/quicktime`
-   `video/x-mpeg`
-   `video/x-mpeg2a`
-   `video/x-ms-asf`
-   `video/x-ms-asf-plugin`
-   `video/x-ms-wm`
-   `video/x-ms-wmv`
-   `video/x-ms-wmx`
-   `video/x-ms-wvx`
-   `video/x-msvideo`

## Examples

This example shows a simple appcontent-ms file that describes an item named "Sample 1".

Notice that the file contains elements not defined by the appcontent-ms schema: `IndexerSampleInformation` and `IndexerSampleSpecificElement`. Your appcontent-ms file must have a root node that encapsulates all the data to be indexed, but you can name that node anything you want.

```XML
<?xml version="1.0" encoding="utf-8"?>
<IndexerSampleInformation>
  <Properties xmlns="http://schemas.microsoft.com/Search/2013/ApplicationContent">
    <Name>Sample 1</Name>
    <Keywords>
      <Keyword xml:lang="en-US">Sample 1 - keyword 1</Keyword>
      <Keyword>Sample 1 - keyword 2</Keyword>
    </Keywords>
    <Comment>Sample 1 comment</Comment>
    <AdditionalProperties>
      <Property Key="System.Title">Sample 1 Title</Property>
      <Property xml:lang="en-US" Key="System.Contact.EmailAddresses">
        <Value>bryan@contoso.com</Value>
        <Value>vincent@contoso.com</Value>
      </Property>
    </AdditionalProperties>
  </Properties>
  <IndexerSampleSpecificElement sc:IndexableContent="true" 
    xmlns:sc="http://schemas.microsoft.com/Search/2013/ApplicationContent">
    The text included here will be indexed, enabling full-text search.
  </IndexerSampleSpecificElement>
</IndexerSampleInformation>
```

You can even tell Windows Search to index the content of arbitrary elements. Just use the [**IndexableContent**](indexablecontent.md) attribute to tell Search to index the content. In the preceding example, Windows Search will index the content of the IndexerSampleSpecificElement because the **IndexableContent** attribute is set to **true**:

```XML
  <IndexerSampleSpecificElement sc:IndexableContent="true" 
    xmlns:sc="http://schemas.microsoft.com/Search/2013/ApplicationContent">
    The text included here will be indexed, enabling full-text search.
  </IndexerSampleSpecificElement>
```

Search will treat the content as text content by default; if the content is base64, use the **ContentType** attribute to specify the MIME type.

The next example shows how to copy an appcontent-ms file to your app's LocalFolder\\Indexed folder. The code copies any files it finds in the app's appcontent-ms folder to the LocalFolder\\Indexed folder. (You can also create new appcontent-ms files directly in the Indexed folder rather than copying them from another location.)

```CSharp
/// <summary>
/// For the purposes of this sample, the appcontent-ms files are stored in an "appcontent-ms" folder in the
/// install directory. These are then copied into the app&#39;s "LocalState\Indexed" folder, which exposes them
/// to the indexer.
/// </summary>
public async static Task<string> AddAppContentFilesToIndexedFolder()
{
    var localFolder = Windows.Storage.ApplicationData.Current.LocalFolder;
    var installDirectory = Windows.ApplicationModel.Package.Current.InstalledLocation;
    var outputString = "Items added to the \"Indexed\" folder:";
    var appContentFolder = await installDirectory.GetFolderAsync("appcontent-ms");
    var indexedFolder = await localFolder.CreateFolderAsync(
        "Indexed", Windows.Storage.CreationCollisionOption.OpenIfExists);
    var files = await appContentFolder.GetFilesAsync();
    foreach (var file in files)
    {
        outputString += "\n" + file.DisplayName + file.FileType;
        await file.CopyAsync(indexedFolder, 
            file.Name, Windows.Storage.NameCollisionOption.ReplaceExisting);
    }
    return outputString;
}
```

```JavaScript
// For the purposes of this sample, the appcontent-ms files are stored in an "appcontent-ms" folder
// in the install directory.  These are then copied into the app&#39;s "LocalState\Indexed" folder,
// which exposes them to the indexer.
function _addAppContentFilesToIndexedFolder() {
    var localFolder = appData.localFolder,
        appcontentFolder,
        indexedFolder,
        installDirectory = Windows.ApplicationModel.Package.current.installedLocation;
    var output = "Items added to the \"Indexed\" folder:\n";
    installDirectory.getFolderAsync("appcontent-ms").then(function (retrievedAppcontentFolder) {
        appcontentFolder = retrievedAppcontentFolder;
        return localFolder.createFolderAsync(
            "Indexed", Windows.Storage.CreationCollisionOption.openIfExists);
    }).then(function (retrievedIndexedFolder) {
        indexedFolder = retrievedIndexedFolder;
        return appcontentFolder.getFilesAsync(appcontentFolder);
    }).then(function (files) {
        var promiseArray = [];
        for (var i = 0, len = files.length; i < len; i++) {
            promiseArray[i] = files[i].copyAsync(indexedFolder, 
                files[i].name, Windows.Storage.NameCollisionOption.replaceExisting);
            output += files[i].displayName + files[i].fileType;
            if (i < len - 1) {
                output += "\n";
            }
        }
        return WinJS.Promise.join(promiseArray);
    }).done(function () {
        WinJS.log &amp;&amp; WinJS.log(output, "sample", "status");
    });
}
```

For the complete code, see the [Indexer sample](https://go.microsoft.com/fwlink/p/?LinkID=311565).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 8.1 [desktop apps only]</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2012 R2 [desktop apps only]</p></td>
</tr>
</tbody>
</table>

## See also


[Indexer sample](https://go.microsoft.com/fwlink/p/?LinkID=311565)

[**Windows.Storage.Search**](https://msdn.microsoft.com/library/windows/apps/br208106)

 

 




