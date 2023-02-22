class Search:

 search = {}
 
 '''
 Search component 1
 '''
 search_1 ="""
import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { clearSearchState } from '../../redux/actions/productActions';

const @@ComponentName@@ = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const navigate = useNavigate();
  const dispatch = useDispatch();

  const searchItems = () => {
    dispatch(clearSearchState())
    navigate(`/search/${searchQuery.trim().toLowerCase()}`);
  }

  const onSearchChange = (e) => {
    const val = e.target.value.trimStart();
    setSearchQuery(val);
  };

  const onFocusInput = (e) => {
    e.target.select();
  };
  
  return (
    <div className="flex justify-center">
        <form id="submitForm" onSubmit={(e) => searchItems(e.target.value)}>
          <div className="flex items-center flex-nowrap">
            <input 
              value={searchQuery}
              onFocus={onFocusInput}
              onChange={onSearchChange}
              type="search" 
              className="focus:ring-green-500 w-full" placeholder="Search" aria-label="Search"
              aria-describedby="search-addon" />
            <button type="submit" className="bg-transparent hover:bg-gray-200 text-green-700 font-semibold hover:text-white py-2 px-2 border border-green-500"><svg xmlns="http://www.w3.org/2000/svg" 
              width="24" height="24" 
              className="hover:text-white">
                <path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z"></path></svg>
            </button>
          </div>
        </form>
    </div>
  )
}

export default @@ComponentName@@;
 """
 search["search_1"] = search_1


 '''
 Search component 2
 '''
 search_2 ="""
Content goes here
 """
 search["search_2"] = search_2
 