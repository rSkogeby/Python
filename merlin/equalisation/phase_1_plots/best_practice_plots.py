import pandas as pd
import matplotlib.style as style
import matplotlib.pyplot as plt

# In Jupyter Notebook: %matplotlib inline

# Set plot style
style.use('fivethirtyeight')



def main():
    direct_link = "percent-bachelors-degrees-women-usa.csv" #'http://www.randalolson.com/wp-content/uploads/percent-bachelors-degrees-women-usa.csv'
    women_majors = pd.read_csv(direct_link)

    #print(women_majors.info())
    #print(women_majors.head())
    #print(women_majors.tail())
    under_20 = women_majors.loc[0, women_majors.loc[0]<20]


    #under_20_graph = women_majors.plot(x = 'Year', y = under_20.index, figsize = (12,8))
    #print('Type:', type(under_20_graph))
    
    # Colorblind-friendly colors
    colors = [[0,0,0], [230/255,159/255,0], [86/255,180/255,233/255], [0,158/255,115/255], 
          [213/255,94/255,0], [0,114/255,178/255]]

    fte_graph = women_majors.plot(x = 'Year', y = under_20.index, figsize = (12,8), color=colors, legend=False)
    fte_graph.tick_params(axis = 'both', which = 'major', labelsize = 18)


    # Customizing the tick labels of the y-axis 
    fte_graph.set_yticklabels(labels = [-10, '0   ', '10   ', '20   ', '30   ', '40   ', '50%'])
    print('The tick labels of the y-axis:', fte_graph.get_yticks()) # -10 and 60 are not visible on the graph
    
    # Generate a bold horizontal line at y = 0 
    fte_graph.axhline(y = 0, color = 'black', linewidth = 1.3, alpha = .7)
    
    # Add an extra vertical line by tweaking the range of the x-axis (NOT NEEDED)
    #fte_graph.set_xlim(left = 1969, right = 2011)

    # Drop xlabel and set xlims
    fte_graph.xaxis.label.set_visible(False)
    fte_graph.set_xlim(left = 1969, right = 2011)

    # The signature bar
    """ fte_graph.text(x = 1965.8, y = -7,
    s = '   ©Quantum Detectors                                                                         Source: National Center for Education Statistics   ',
    fontsize = 14, color = '#f0f0f0', backgroundcolor = 'grey') """
    
    # The other signature bar
    fte_graph.text(x = 1966.1, y = -6.5,
    s = '__________________________________________________________________________________________________________________________________________________________________________',
    color = 'grey', alpha = .7)

    fte_graph.text(x = 1966.1, y = -9,
    s = '   ©Quantum Detectors                                                                         Source: National Center for Education Statistics   ',
    fontsize = 14, color = 'grey', alpha = .7)

    # Adding a title and a subtitle
    fte_graph.text(x = 1966.65, y = 62.7, s = "The gender gap is transitory - even for extreme cases",
               fontsize = 26, weight = 'bold', alpha = .75)
    fte_graph.text(x = 1966.65, y = 57, 
               s = 'Percentage of Bachelors conferred to women from 1970 to 2011 in the US for\nextreme cases where the percentage was less than 20% in 1970',
              fontsize = 19, alpha = .85)


    # Add colored labels
    fte_graph.text(x = 1994, y = 44, s = 'Agriculture', color = colors[0], weight = 'bold', rotation = 33,
              backgroundcolor = '#f0f0f0')
    fte_graph.text(x = 1985, y = 42.2, s = 'Architecture', color = colors[1], weight = 'bold', rotation = 18,
              backgroundcolor = '#f0f0f0')
    fte_graph.text(x = 2004, y = 51, s = 'Business', color = colors[2], weight = 'bold', rotation = -5, 
               backgroundcolor = '#f0f0f0')
    fte_graph.text(x = 2001, y = 30, s = 'Computer Science', color = colors[3], weight = 'bold', rotation = -42.5,
              backgroundcolor = '#f0f0f0')
    fte_graph.text(x = 1987, y = 11.5, s = 'Engineering', color = colors[4], weight = 'bold',
              backgroundcolor = '#f0f0f0')
    fte_graph.text(x = 1976, y = 25, s = 'Physical Sciences', color = colors[5], weight = 'bold', rotation = 27,
              backgroundcolor = '#f0f0f0')

    plt.show()

if __name__=='__main__':
    main()