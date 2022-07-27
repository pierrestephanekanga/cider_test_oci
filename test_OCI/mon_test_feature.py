#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sys
sys.path.insert(0, '../../cider/cider')
sys.path.insert(0, '../../cider')


# In[5]:


from datastore import DataStore
from featurizer import Featurizer


# In[ ]:


datastore = DataStore(cfg_dir='../../cider/test_OCI/config-mon-test.yml')


# In[ ]:


featurizer = Featurizer(datastore=datastore, clean_folders=True)


# In[ ]:


featurizer.ds.cdr.show(5)


# In[ ]:


featurizer.ds.mobilemoney.show(3)


# In[ ]:


featurizer.ds.mobiledata.show(3)


# In[ ]:


featurizer.ds.recharges.show(3)


# In[ ]:


featurizer.ds.shapefiles['districts'].head(3)


# In[ ]:


featurizer.ds.shapefiles['regions'].head(3)


# In[ ]:


featurizer.ds.shapefiles['departements'].head(3)


# In[ ]:


featurizer.ds.shapefiles['communes'].head(3)


# In[ ]:


featurizer.ds.antennas.show(3)


# In[ ]:


# Deduplication
featurizer.ds.deduplicate()

# Filter to just January 1 - February 28 (inclusive)
featurizer.ds.filter_dates('2022-05-17', '2022-05-19')

# Remove transactions involving spammers who place 1.8+ calls/texts per active day
#spammers = featurizer.ds.remove_spammers(spammer_threshold=1.8)


# In[ ]:


# Remove all records from days more than 2 standard deviations from the mean transaction volume
outlier_days = featurizer.ds.filter_outlier_days(num_sds=2)


# In[ ]:


print(featurizer.diagnostic_statistics())


# In[ ]:


featurizer.diagnostic_plots()


# In[ ]:


featurizer.recharges_features()


# In[ ]:


featurizer.mobiledata_features()


# In[ ]:


featurizer.mobilemoney_features()


# In[ ]:


#featurizer.location_features()


# In[ ]:


featurizer.international_features()


# In[ ]:


featurizer.cdr_features()


# In[ ]:


featurizer.all_features()


# In[ ]:


#import pandas as pd
#pd.read_csv('./outputs/featurizer/datasets/features.csv').head()


# In[ ]:


#dfe = featurizer.features['mobilemoney'].toPandas()


# In[ ]:


#dfe.to_csv('dfe.csv', index=False)


# In[ ]:


#dfe.columns.tolist()


# In[ ]:


#dfe['mobilemoney_all_cashout_txns']


# In[ ]:


featurizer.feature_plots()


# In[ ]:




