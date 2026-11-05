# API versioning

API versioning enables TikTok Shop to continuously improve and expand API capabilities while maintaining a seamless integration experience as APIs evolve.
When breaking changes are introduced to TikTok Shop APIs, these changes are rolled out through new API versions. Breaking changes may be necessary to improve functionality, introduce new capabilities, or enhance security. To keep integrations stable and benefit from newer capabilities, developers should regularly review supported versions and upgrade when needed.
For examples of both non-breaking and breaking changes, use the [changelog](https://partner.tiktokshop.com/docv2/changelog) as the source of truth instead of relying on fixed examples in this page. Changelog entries are updated over time and may include categories such as API updates, new endpoint releases, field additions, migration notices, breaking changes, and retirement notices.
# API release schedule and version naming
New API versions are generally rolled out on a monthly basis, but not every API is updated every month.
The API version name, such as `202303`, is derived from the year and month when that API version was launched.
# Selecting API versions in API reference docs
API versions are assigned at the API level, meaning different APIs may support different version lists at the same time. Do not use a hardcoded example to decide the latest version of an API.
The API reference page displays the latest supported version of that API by default. Use the version dropdown menu on the reference page to confirm which versions are currently supported for the API you are calling. By clicking a version name in the dropdown menu, you can access the reference doc for that specific API version.
Different APIs from different versions can generally be used together, but integrations should be tested thoroughly. In most cases, use the latest supported version shown on the API reference page for each endpoint. If your integration depends on multiple related APIs, test the version combination before release.
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/fdd7aa43e905434bbca6f2d5b67b6a6d~tplv-k9wyc2ijk0-image.image)
# Specifying an API version when calling an API
Starting with the `202309` API style, the API version is part of the request path. For more migration details, refer to Upgrading to 202309 and Methods and endpoints.
Use the endpoint path exactly as shown in the API reference page when generating the request signature.
| API style | URI pattern | Version location |
| --- | --- | --- |
| Legacy API style | `https://open-api.tiktokglobalshop.com/{legacy_resource}?version={version}&app_key={app_key}&timestamp={timestamp}&sign={sign}` | Query parameter |
| `202309` and later API style | `https://open-api.tiktokglobalshop.com/{category}/{version}/{resource}?app_key={app_key}&timestamp={timestamp}&sign={sign}` | Path segment |
Example for the `202309` and later API style:
```HTTP
GET https://open-api.tiktokglobalshop.com/authorization/202309/shops?app_key={app_key}&timestamp={timestamp}&sign={sign}
```

When calculating the signature for `202309` and later APIs, include the path exactly as shown after the host, including the category, version, and resource segments, for example `/authorization/202309/shops`.
# Upgrading to a new API version
Before upgrading to a new API version, read both the changelog and the API reference docs for the target version. Check for changes in path, method, headers, query parameters, request body, response body, error codes, field meanings, market availability, and authorization scope requirements.
Use the version dropdown menu on the API reference page to compare supported versions of the same API. If a separate migration guide is available, such as Upgrading to 202309, follow that guide together with the endpoint reference page.
# Retiring a version of an API
After a new version of an API is released, the prior version remains available for a minimum of 2 months. This is the minimum availability window counted from the new version release.
When an API version is scheduled for permanent retirement, the retirement announcement is communicated through the [changelog](https://partner.tiktokshop.com/docv2/changelog) at least 2 months before the permanent retirement date. This is the retirement notice window counted backward from the permanent retirement date.
These two 2-month windows describe different lifecycle checkpoints. They should be read as the following timeline:
| Timeline node | What happens | Timing rule |
| --- | --- | --- |
| 1. New version released | A newer API version becomes available in the API reference page. | Start of the new version lifecycle. |
| 2. Prior version minimum availability | The prior version remains callable after the new version release. | Minimum 2 months after the new version release. |
| 3. Retirement announcement | If the prior version is scheduled for permanent retirement, a changelog notice is posted. | At least 2 months before permanent retirement. |
| 4. Permanent retirement | The retired version is no longer supported. Calls to that version may fail. | Effective on the retirement date stated in the changelog. |
If you use a retired or invalid version, the API may return an error indicating that the API version is not supported.
```JSON
{
  "code": 36009014,
  "data": null,
  "message": "The version name is invalid, please check and retry."
}
```

Some common gateway or legacy examples may surface `36009004` with an `Invalid API version` message for the same general condition. Until the runtime behavior is fully aligned across docs and endpoints, handle invalid-version failures by checking both the response `code` and the `message` text, and log the `request_id` for troubleshooting. This should be kept consistent with Common errors.
# Staying updated
## Changelog
The [changelog](https://partner.tiktokshop.com/docv2/changelog) is the primary source for API changes, including new versions, new endpoints, non-breaking updates, migration notices, breaking changes, and retirement notices. Regularly checking the changelog helps you plan upgrades early and avoid calling retired versions.
