--[[
This program:
- Sets the level-one header as title and ignores it as header, promoting all
  other headers by one level;
- Raises an error if there are multiple level-one headers;
- Raises an error if the title is not declared (checking metadata and headers).
]]--

local title

local function promote_header (header)
  if header.level >= 2 then
    header.level = header.level - 1
    return header
  end
  return {}
end

local function get_header_title (header)
  if header.level == 1 then
    if not title then
      title = header.content
    else
      error("More than one title declaration found")
    end
  end
  return header
end

local function get_metadata_title (meta)
  title = meta.title
end

local function set_metadata_title (meta)
  if title then
    meta.title = title
  else
    error("No title was found")
  end
end

return {
  {Meta = get_metadata_title},
  {Header = get_header_title},
  {Header = promote_header},
  {Meta = set_metadata_title},
}
