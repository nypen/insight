import React from 'react';
import { CircularProgress, Divider, Grid, makeStyles, Theme, Typography } from '@material-ui/core';
import { AppBar } from './appBar';
import { getUrl } from '../appServices';
import { RequestFormType } from '../requestForm';
import { RequestForm } from './requestForm';
import JSONPretty from 'react-json-pretty';
import purple from '@material-ui/core/colors/purple';

const useStyles = makeStyles((theme: Theme) => ({
    root: {
        height: "100vh",
        backgroundColor: theme.palette.grey[700],
    },
    requestForm: {
        height: "90vh",
        backgroundColor: "#FFF",
    }

}));

interface MainProps { }

const Main = (props: React.PropsWithChildren<MainProps>) => {
    const [error, setError] = React.useState(null);
    const [loading, setLoading] = React.useState(false);
    const [result, setResult] = React.useState(null);

    const classes = useStyles();

    const theme = {
        main: "line-height:1.3;background:#FFF;overflow:auto;",
        key: `color:${purple[700]}`,
    };

    const handleonClick = (requestForm: RequestFormType) => {
        setLoading(true);
        setResult(null);

        fetch(getUrl(requestForm.id), {
            method: 'POST',
            cache: "no-cache",
            body: JSON.stringify({ username: requestForm.username, password: requestForm.password, isSentinel5P: requestForm.isSentinel5P }),
            headers: new Headers({
                'mode': 'cors',
                'Content-Type': 'application/json'
            })
        })
            .then(
                (result) => {
                    const jsonResult = result.json()
                    console.log("result " + jsonResult);
                    return jsonResult;
                },
                (error) => {
                    console.log("Error" + error);
                    setLoading(false);
                    setError(error);
                }
            )
            .then(
                // TODO: Fix loading remaining true after error response
                (data) => {
                    setLoading(false);
                    setResult(data);
                    console.log(data)
                }
            )
    }

    return (
        <div>
            <Grid container className={classes.root} justify="center" xs={12}>
                <Grid item xs={12}>
                    <AppBar />
                </Grid>
                <Grid item container className={classes.requestForm}  direction="row" justify="center" alignItems="center" xs={10}>
                    <Grid item style={{width:"45%"}}>
                        <RequestForm
                            loading={loading}
                            submitRequest={handleonClick}
                        />
                    </Grid>
                    <Divider orientation="vertical"  style={{marginRight:"-1px"}} />
                    <Grid item container justify="center" alignItems="center" style={{width:"55%"}}>
                        <Grid item >
                            {result &&
                                <JSONPretty style={{padding:"10px", height:"100%"}}
                                    themeClassName="custom-json-pretty"
                                    theme={theme}
                                    data={result["result"]}/>
                            }
                            {
                                loading && <CircularProgress size={60} color="secondary" />
                            }
                            <Typography color="error">
                                {error && error.message}
                            </Typography>
                        </Grid>
                    </Grid>
                </Grid>
            </Grid>
        </div>
    );
}

export { Main }