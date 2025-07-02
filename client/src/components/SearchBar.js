import React from 'react';

const SearchBar = ({ search, setSearch, onSearch }) => (
  <input
    placeholder="Search"
    value={search}
    onChange={(e) => {
      setSearch(e.target.value);
      onSearch(e.target.value);
    }}
  />
);

export default SearchBar;
